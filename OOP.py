from Utility import calcola_durata_minuti, classifica_corsa, riepilogo_corse, stampa_riepilogo_analisi

# Classe Padre Bicicletta
class Bicicletta:

# Attributi nel __init__:
# - id_bici: str — es. "MI-042"
# - tipo: str — "classica" o "elettrica"
# - stazione_corrente: str
# - km_percorsi: float
# - disponibile: bool

    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool):
        self.id_bici = id_bici
        self.tipo = tipo
        self.stazione_corrente = stazione_corrente

        # Aggiunta Incapsulamento
        self._km_percorsi = km_percorsi

        self.disponibile = disponibile

# Metodi obbligatori:
# - noleggia(self, utente: str) -> str — imposta disponibile = False; solleva ValueError se già in uso
# - restituisci(self, stazione: str, km_aggiunti: float) -> None — aggiorna stazione e km
# - __str__ — es. "[MI-042] elettrica | Cadorna | 342.5 km | ✓ disponibile"
# - __repr__

    def noleggia(self, utente: str) -> str:

        if not self.disponibile:
            raise ValueError("Bicicletta già in uso")

        self.disponibile = False

        return f"Bicicletta {self.id_bici} noleggiata da {utente}"

    def restituisci(self, stazione: str, km_aggiunti: float):
        self.stazione_corrente = stazione

        # Aggiunta parte incapsulamento
        self.aggiungi_km(km_aggiunti)

        self.disponibile = True

    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

    def __repr__(self):
        return f"Bicicletta({self.id_bici}, {self.tipo}, {self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"

    # Rinomina km_percorsi → _km_percorsi
    # Crea @property km_percorsi in sola lettura
    # Crea aggiungi_km(self, km: float) -> None — valida che km > 0 prima di aggiornare

    @property
    def km_percorsi(self):
        return self._km_percorsi

    def aggiungi_km(self, km: float):
        if km <= 0:
            raise ValueError("I km devono essere positivi")

        self._km_percorsi += km

# Classi Figlie di Bicicletta
class BiciclettaClassica(Bicicletta):

    # Aggiunge attributo taglia: str ("S", "M", "L")
    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool, taglia: str):
        super().__init__(id_bici, tipo, stazione_corrente, km_percorsi, disponibile)
        self.taglia = taglia

    # Override di __str__ e __repr__ per includere la taglia
    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} | taglia: {self.taglia} | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

    def __repr__(self):
        return f"BiciclettaClassica({self.id_bici}, {self.tipo}, {self.taglia},{self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"


class BiciclettaElettrica(Bicicletta):

    # Aggiunge attributo batteria_percentuale: int (0–100)
    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool, batteria_percentuale: int):
        super().__init__(id_bici, tipo, stazione_corrente, km_percorsi, disponibile)
        self.batteria_percentuale = batteria_percentuale

    # - Aggiunge ricarica(self, percentuale: int) -> None (massimo 100)
    def ricarica(self, percentuale: int):

        if percentuale < 0:
            raise ValueError("La percentuale della batteria non può avere valori negativi")

        else:
            self.batteria_percentuale += percentuale
            if self.batteria_percentuale > 100:
                self.batteria_percentuale = 100

    # - Override di __str__ e __repr__ per mostrare livello batteria, es. 🔋 78%
    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} |🔋{self.batteria_percentuale}% | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

    def __repr__(self):
        return f"BiciclettaElettrica({self.id_bici}, {self.tipo}, {self.batteria_percentuale}, {self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"

    # - Override di noleggia — solleva ValueError se batteria_percentuale < 20
    def noleggia(self, utente: str) -> str:

        if not self.disponibile:
            raise ValueError("Bicicletta già in uso")

        if self.batteria_percentuale < 20:
            raise ValueError("Questa bicicletta non ha carica sufficiente")

        self.disponibile = False

        return f"Bicicletta {self.id_bici} noleggiata da {utente}"


# Classe di gestione delle bici
class FlottaBici:

# Attributi:
# - biciclette: list
# - citta: str

    def __init__(self, biciclette: list, citta: str):
        self.biciclette = biciclette
        self.citta = citta

# Metodi obbligatori:
# - aggiungi(self, bici: Bicicletta) -> None
# - rimuovi(self, id_bici: str) -> None — solleva KeyError se non trovata
# - cerca_per_id(self, id_bici: str) -> Bicicletta — solleva KeyError se non trovata
# - disponibili(self) -> list
# - statistiche(self) -> dict — chiavi: totale, disponibili, in_uso, km_totali_flotta, km_medi_per_bici
# - __len__
# - @classmethod da_lista(cls, citta: str, dati: list) -> "FlottaBici" — costruisce la flotta da una lista
#   di dizionari con chiavi id, tipo, stazione, km

    def aggiungi(self, bici: Bicicletta):

        if not isinstance(bici, Bicicletta):
            raise TypeError("Stai cercando di aggiungere un oggetto diverso da una bicicletta")

        # controllo duplicati
        for b in self.biciclette:
            if b.id_bici == bici.id_bici:
                raise ValueError(f"Bicicletta con id {bici.id_bici} già presente nella flotta")

        self.biciclette.append(bici)

    def rimuovi(self, id_bici: str):

        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                self.biciclette.remove(bici)
                return
        else:
            raise KeyError("Bicicletta non trovata")

    def cerca_per_id(self, id_bici: str) -> Bicicletta:

        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                return bici
        else:
            raise KeyError("Bicicletta non trovata")

    def disponibili(self) -> list:

        lista_disponibili = []

        for bici in self.biciclette:
            if bici.disponibile:
                lista_disponibili.append(bici)

        return lista_disponibili

    def statistiche(self) -> dict:

        totale = len(self.biciclette)
        disponibili = len(self.disponibili())
        in_uso = totale - disponibili

        km_totali = 0

        for bici in self.biciclette:
            km_totali += bici.km_percorsi

        if totale > 0:
            km_medi = km_totali / totale

        else:
            km_medi = 0

        return {
            "totale": totale,
            "disponibili": disponibili,
            "in_uso": in_uso,
            "km_totali_flotta": km_totali,
            "km_medi_per_bici": km_medi
        }

    def __len__(self):
        return len(self.biciclette)

    @classmethod
    def da_lista(cls, citta: str, dati: list) -> "FlottaBici":

        biciclette = []

        for dato in dati:

            tipo = dato.get("tipo")

            if tipo is None:
                raise ValueError("Tipo bicicletta mancante")

            if tipo == "classica":
                bici = BiciclettaClassica(
                    id_bici = dato["id"],
                    tipo = tipo,
                    stazione_corrente = dato["stazione"],
                    km_percorsi = dato["km"],
                    disponibile = dato["disponibile"],
                    taglia = dato["taglia"]
                )
                biciclette.append(bici)

            elif tipo == "elettrica":
                bici = BiciclettaElettrica(
                    id_bici = dato["id"],
                    tipo = tipo,
                    stazione_corrente = dato["stazione"],
                    km_percorsi = dato["km"],
                    disponibile = dato["disponibile"],
                    batteria_percentuale = dato["batteria"]
                )
                biciclette.append(bici)

            else:
                raise ValueError(f"Tipo bicicletta non valido: {tipo}")

        return cls(biciclette, citta)

# Realizza una piccola dimostrazione di polimorfismo:

# def stampa_flotta(biciclette: list) -> None:
#     ...

#     Crea una lista con oggetti di almeno 2 classi diverse del dominio
#     Applica la stessa operazione a tutti gli elementi senza fare controlli espliciti sul tipo
#     Inserisci un commento breve (2-3 righe) in cui spieghi l'idea di interfaccia comune e dispatch dinamico
#     Mostra anche una chiamata di esempio della funzione

b1 = Bicicletta("A1", "classica", "Duomo", 10, True)
b2 = BiciclettaClassica("A2", "classica", "Centrale", 20, True, "M")
b3 = BiciclettaElettrica("A3", "elettrica", "Porta Nuova", 15, True, 80)

flotta = [b1, b2, b3]

def stampa_flotta(biciclette: list):
    for bici in biciclette:
        print(bici)

stampa_flotta(flotta)

print()
print()
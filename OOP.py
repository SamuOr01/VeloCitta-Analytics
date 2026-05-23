# Task 2 — OOP Parte 1: Record e Dataset

# 2.1 — Classe Bicicletta — pattern Record

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

        # 3.2 — Incapsulamento
        # Rinomina km_percorsi -> _km_percorsi
        self._km_percorsi = km_percorsi

        self.disponibile = disponibile


# Metodi obbligatori:
# - noleggia(self, utente: str) -> str — imposta disponibile = False; solleva ValueError se già in uso
# - restituisci(self, stazione: str, km_aggiunti: float) -> None — aggiorna stazione e km
# - __str__ — es. "[MI-042] elettrica | Cadorna | 342.5 km | ✓ disponibile"
# - __repr__

    # Funzione per il noleggio della bici
    def noleggia(self, utente: str) -> str:

        # Solleva un eccezione se già in uso
        if not self.disponibile:
            raise ValueError("Bicicletta già in uso")

        # Imposta la bici come non disponibile
        self.disponibile = False

        # restituisce l'informazione
        return f"Bicicletta {self.id_bici} noleggiata da {utente}"


    # Funzione per la restituzione della bici
    def restituisci(self, stazione: str, km_aggiunti: float):

        # Aggiorna la stazione corrente
        self.stazione_corrente = stazione

        # Aggiunta parte incapsulamento
        # Chiama il metodo per aggiungere km percorsi
        self.aggiungi_km(km_aggiunti)

        # Imposta la bici come nuovamente disponibile
        self.disponibile = True


    # Rappresentazione leggibile (__str__) per utenti
    def __str__(self):

        # Se disponibile
        if self.disponibile:

            # Stampa
            stato = "✅ Disponibile"

        # Altrimenti
        else:

            # Stampa
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"


    # Rappresentazione tecnica (__repr__) per debug
    def __repr__(self):
        return f"Bicicletta({self.id_bici}, {self.tipo}, {self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"


    # 3.2 — Incapsulamento
    # Crea @property km_percorsi in sola lettura
    # Crea aggiungi_km(self, km: float) -> None — valida che km > 0 prima di aggiornare

    # Property in sola lettura
    @property
    def km_percorsi(self):
        return self._km_percorsi

    # Metodo per aggiungere km percorsi
    def aggiungi_km(self, km: float):

        # Solleva un eccezione se km non è maggiore di 0
        if km <= 0:
            raise ValueError("I km devono essere positivi")

        # Effettua la somma
        self._km_percorsi += km


# Task 3 — OOP Parte 2: Ereditarietà, Incapsulamento, Polimorfismo

# 3.1 — Ereditarietà

# Crea due sottoclassi di Bicicletta:

# BiciclettaClassica(Bicicletta):

#   - Aggiunge attributo taglia: str ("S", "M", "L")
#   - Override di __str__ per includere la taglia

# Classe Figlia di Bicicletta
class BiciclettaClassica(Bicicletta):

    # Aggiunge attributo 'taglia'
    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool, taglia: str):
        super().__init__(id_bici, tipo, stazione_corrente, km_percorsi, disponibile)
        self.taglia = taglia


    # Override __str__ per includere la taglia
    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} | taglia: {self.taglia} | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"


    # Override __repr__ per includere la taglia
    def __repr__(self):
        return f"BiciclettaClassica({self.id_bici}, {self.tipo}, {self.taglia},{self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"


# BiciclettaElettrica(Bicicletta):

#   - Aggiunge attributo batteria_percentuale: int (0–100)
#   - Aggiunge ricarica(self, percentuale: int) -> None (massimo 100)
#   - Override di __str__ per mostrare livello batteria, es. 🔋 78%
#   - Override di noleggia — solleva ValueError se batteria_percentuale < 20

# Classe Figlia di Bicicletta
class BiciclettaElettrica(Bicicletta):

    # Aggiunge batteria
    def __init__(self, id_bici: str, tipo: str, stazione_corrente: str, km_percorsi: float, disponibile: bool, batteria_percentuale: int):
        super().__init__(id_bici, tipo, stazione_corrente, km_percorsi, disponibile)
        self.batteria_percentuale = batteria_percentuale


    # Metodo per ricaricare la batteria (max 100%)
    def ricarica(self, percentuale: int):

        # Solleva un eccezione se la percentuale è negativa
        if percentuale < 0:
            raise ValueError("La percentuale della batteria non può avere valori negativi")

        # Altrimenti somma la percentuale
        else:
            self.batteria_percentuale += percentuale

            # Limite massimo alla carica della batteria impostato a 100
            if self.batteria_percentuale > 100:
                self.batteria_percentuale = 100


    # Override __str__ per mostrare batteria
    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} |🔋{self.batteria_percentuale}% | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

    # Override __repr__ per mostrare batteria
    def __repr__(self):
        return f"BiciclettaElettrica({self.id_bici}, {self.tipo}, {self.batteria_percentuale}, {self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"


    # Override noleggio
    def noleggia(self, utente: str) -> str:

        if not self.disponibile:
            raise ValueError("Bicicletta già in uso")

        # Aggiunto controllo che solleva un eccezione se la carica non è sufficiente
        if self.batteria_percentuale < 20:
            raise ValueError("Questa bicicletta non ha carica sufficiente")

        self.disponibile = False

        return f"Bicicletta {self.id_bici} noleggiata da {utente}"


# 2.2 — Classe FlottaBici — pattern Dataset

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

    # Aggiunge bici alla flotta
    def aggiungi(self, bici: Bicicletta):

        # Solleva un eccezione se l'oggetto non è di tipo bicicletta
        if not isinstance(bici, Bicicletta):
            raise TypeError("Stai cercando di aggiungere un oggetto diverso da una bicicletta")

        # # Solleva un eccezione se ci sono duplicati
        for b in self.biciclette:
            if b.id_bici == bici.id_bici:
                raise ValueError(f"Bicicletta con id {bici.id_bici} già presente nella flotta")

        # Aggiunge la bici alla flotta
        self.biciclette.append(bici)


    # Rimuove la bici dalla flotta
    def rimuovi(self, id_bici: str):

        # Effettuando un controllo per id
        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                self.biciclette.remove(bici)
                return

        # Se non viene trovata alcuna corrispondenza solleva un eccezione
        else:
            raise KeyError("Bicicletta non trovata")


    # Cerca le bici
    def cerca_per_id(self, id_bici: str) -> Bicicletta:

        # Effettuando un controllo per id
        for bici in self.biciclette:

            if bici.id_bici == id_bici:
                return bici

        # Se non viene trovata alcuna corrispondenza solleva un eccezione
        else:
            raise KeyError("Bicicletta non trovata")


    # Funzione per stampare l'elenco delle bici disponibili
    def disponibili(self) -> list:

        lista_disponibili = []

        # Effettuando un controllo nella flotta
        for bici in self.biciclette:

            # Se la bici è disponibile l'aggiunge all'elenco
            if bici.disponibile:
                lista_disponibili.append(bici)

        return lista_disponibili


    # Stampa le statistiche generali della flotta
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


    # Permette di stampare la lunghezza dell'oggetto
    def __len__(self):
        return len(self.biciclette)


    # Metodo di classe che costruisce la flotta da lista di dati
    @classmethod
    def da_lista(cls, citta: str, dati: list) -> "FlottaBici":

        biciclette = []

        for dato in dati:

            tipo = dato.get("tipo")

            if tipo is None:
                raise ValueError("Tipo bicicletta mancante")

            if tipo == "Classica":
                bici = BiciclettaClassica(
                    id_bici = dato["id"],
                    tipo = tipo,
                    stazione_corrente = dato["stazione"],
                    km_percorsi = dato["km"],
                    disponibile = dato["disponibile"],
                    taglia = dato["taglia"]
                )
                biciclette.append(bici)

            elif tipo == "Elettrica":
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


# 3.3 — Polimorfismo

# Realizza una piccola dimostrazione di polimorfismo:

# def stampa_flotta(biciclette: list) -> None:
#     ...

#     Crea una lista con oggetti di almeno 2 classi diverse del dominio
#     Applica la stessa operazione a tutti gli elementi senza fare controlli espliciti sul tipo
#     Inserisci un commento breve (2-3 righe) in cui spieghi l'idea di interfaccia comune e dispatch dinamico
#     Mostra anche una chiamata di esempio della funzione

# Esempio di creazione flotta mista
b1 = Bicicletta("A1", "classica", "Duomo", 10, True)
b2 = BiciclettaClassica("A2", "classica", "Centrale", 20, True, "M")
b3 = BiciclettaElettrica("A3", "elettrica", "Porta Nuova", 15, True, 80)

flotta = [b1, b2, b3]

# Funzione dimostrativa di polimorfismo
# Tutti gli oggetti hanno la stessa interfaccia (__str__ e noleggia/restituisci)
# Il dispatch dinamico permette di chiamare il metodo corretto senza controllare il tipo
def stampa_flotta(biciclette: list):
    for bici in biciclette:
        print(bici)

# Stampa tutte le bici senza controllare il tipo
stampa_flotta(flotta)

# Righe vuote per output più pulito
print()
print()
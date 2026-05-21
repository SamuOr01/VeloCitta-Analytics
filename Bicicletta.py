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
        self.km_percorsi = km_percorsi
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
        self.km_percorsi += km_aggiunti
        self.disponibile = True

    def __str__(self):
        if self.disponibile:
            stato = "✅ Disponibile"

        else:
            stato = "❌ Non Disponibile"

        return f"[{self.id_bici}] {self.tipo} | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

    def __repr__(self):
        return f"Bicicletta({self.id_bici}, {self.tipo}, {self.stazione_corrente}, {self.km_percorsi}, {self.disponibile})"


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

        return f"[{self.id_bici}] {self.tipo} | 🔋{self.batteria_percentuale}% | {self.stazione_corrente} | {self.km_percorsi:.2f} km | {stato}"

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






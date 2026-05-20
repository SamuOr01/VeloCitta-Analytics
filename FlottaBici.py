# Import delle classi Bicicletta
from Bicicletta import Bicicletta

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

        if bici:
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
            bici = Bicicletta(
                dato["id"],
                dato["tipo"],
                dato["stazione"],
                dato["km"],
                dato["disponibile"]
            )
            biciclette.append(bici)

        return cls(biciclette, citta)
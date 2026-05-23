import numpy as np
from numpy.typing import NDArray

# Task 1 — Setup & Python Base

# 1.2 — Funzioni di utilità

# Scrivi queste tre funzioni senza librerie esterne:

# - calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int

#     - Formato input: "HH:MM"
#     - Solleva ValueError se ora_fine è precedente a ora_inizio

# Funzione per calcoalre la durata della corsa
def calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int:

    # Separazione ore e minuti dell'orario di inizio
    parti_inizio = ora_inizio.split(":")

    # Separazione ore e minuti dell'orario di fine
    parti_fine = ora_fine.split(":")

    # Conversione in interi
    h_inizio = int(parti_inizio[0])
    m_inizio = int(parti_inizio[1])

    h_fine = int(parti_fine[0])
    m_fine = int(parti_fine[1])

    # Conversione totale in minuti
    minuti_inizio = h_inizio * 60 + m_inizio
    minuti_fine = h_fine * 60 + m_fine

    # Controllo validità: la fine non può essere prima dell'inizio
    if minuti_fine < minuti_inizio:
        raise ValueError("L'ora di fine non può precedere l'ora di inizio")

    # Restituisce la differenza dei minuti
    return minuti_fine - minuti_inizio


# - classifica_corsa(durata_minuti: int) -> str

#     - "breve" se < 15 min, "media" se 15–45 min, "lunga" se > 45 min

# Funzione per classificare la durata della corsa
def classifica_corsa(durata_minuti: int) -> str:

    # Controllo input negativo
    if durata_minuti < 0:
        raise ValueError("La durata non può essere negativa")

    # Classificazione per intervalli
    elif durata_minuti < 15:
        return "breve"

    elif durata_minuti <= 45:
        return "media"

    else:
        return "lunga"


# - riepilogo_corse(lista_durate: list) -> dict

#     - Chiavi restituite: totale, media, max, min, brevi, medie, lunghe

# Funzione per riepilogo corsa
def riepilogo_corse(lista_durate: list) -> dict:

    # Controllo lista vuota
    if not lista_durate:
        raise ValueError("La lista delle durate è vuota")

    # Statistiche base
    totale = sum(lista_durate)
    media = totale / len(lista_durate)
    massimo = max(lista_durate)
    minimo = min(lista_durate)

    # Contatori categorie
    brevi = 0
    medie = 0
    lunghe = 0

    # Classificazione di ogni durata
    for durata in lista_durate:
        categoria = classifica_corsa(durata)

        if categoria == "breve":
            brevi += 1
        elif categoria == "media":
            medie += 1
        else:
            lunghe += 1

    # Restituisce un dizionario con il riepilogo
    return {
        "totale": totale,
        "media": media,
        "max": massimo,
        "min": minimo,
        "brevi": brevi,
        "medie": medie,
        "lunghe": lunghe
    }

# Funzione aggiuntiva per l'analisi
def stampa_riepilogo_analisi(array: NDArray, nome: str):

    # Output formattato con statistiche principali
    print(f"L'array {nome}: {array}\n"
          f"\nForma dell'array {nome}: {array.shape}\n"
          f"\nTipo dell'array {nome}: {array.dtype}\n"
          f"\nMinimo dell'array {nome}: {array.min()}\n"
          f"\nMassimo dell'array {nome}: {array.max()}\n"
          f"\nMedia dell'array {nome}: {array.mean()}\n"
          f"\nStandard Deviation dell'array {nome}: {array.std()}\n"
          )
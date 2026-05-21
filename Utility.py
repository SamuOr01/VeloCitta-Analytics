# FUNZIONI DI UTILITÀ


# Funzione per calcoalre la durata della corsa
def calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int:
    # Formato input: "HH:MM"
    # Solleva ValueError se ora_fine è precedente a ora_inizio

    parti_inizio = ora_inizio.split(":")
    parti_fine = ora_fine.split(":")

    h_inizio = int(parti_inizio[0])
    m_inizio = int(parti_inizio[1])

    h_fine = int(parti_fine[0])
    m_fine = int(parti_fine[1])

    minuti_inizio = h_inizio * 60 + m_inizio
    minuti_fine = h_fine * 60 + m_fine

    if minuti_fine < minuti_inizio:
        raise ValueError("L'ora di fine non può precedere l'ora di inizio")

    return minuti_fine - minuti_inizio


# Funzione per classificare la durata della corsa
def classifica_corsa(durata_minuti: int) -> str:
    # "breve" se < 15 min, "media" se 15–45 min, "lunga" se > 45 min

    if durata_minuti < 0:
        raise ValueError("La durata non può essere negativa")

    elif durata_minuti < 15:
        return "breve"

    elif durata_minuti <= 45:
        return "media"

    else:
        return "lunga"


# Funzione per riepilogo corsa
def riepilogo_corse(lista_durate: list) -> dict:
    # Chiavi restituite: totale, media, max, min, brevi, medie, lunghe

    if not lista_durate:
        raise ValueError("La lista delle durate è vuota")

    totale = sum(lista_durate)
    media = totale / len(lista_durate)
    massimo = max(lista_durate)
    minimo = min(lista_durate)

    brevi = 0
    medie = 0
    lunghe = 0

    for durata in lista_durate:
        categoria = classifica_corsa(durata)

        if categoria == "breve":
            brevi += 1
        elif categoria == "media":
            medie += 1
        else:
            lunghe += 1

    return {
        "totale": totale,
        "media": media,
        "max": massimo,
        "min": minimo,
        "brevi": brevi,
        "medie": medie,
        "lunghe": lunghe
    }
# Task 6 — Pandas: Caricamento, Pulizia e Analisi

import pandas as pd
import numpy as np
from numpy import random
from Utility import classifica_corsa


# 6.1 — Creazione DataFrame

# Crea tre DataFrame direttamente via codice (no file CSV esterni).

# df_corse — almeno 80 righe:

#   - Colonne: id_corsa, id_bici, id_utente, citta, data_corsa,
#       durata_minuti, km_percorsi, fascia_oraria
#   - Vincoli: almeno 3 date, 3 città (Milano / Roma / Torino),
#       5 duplicati, 8 NaN sparsi tra durata_minuti e km_percorsi

citta = ["Milano", "Roma", "Torino"]
fasce = ["Mattina", "Pomeriggio", "Sera"]

structure_corse = {
    "id_corsa" : range(1, 81),
    "id_bici" : random.randint(1, 21, 80),
    "id_utente" : random.randint(1, 26, 80),
    "citta" : random.choice(citta, 80),
    "data_corsa" : random.choice(["2026-04-28", "2026-06-14", "2026-09-11", "2026-12-31"], 80),
    "durata_minuti" : np.round(random.uniform(5, 90, 80), 2),
    "km_percorsi" : np.round(random.uniform(1, 20, 80), 2),
    "fascia_oraria" : random.choice(fasce, 80)
}

df_corse = pd.DataFrame(structure_corse)

# Inserimento NaN
indici_durata = random.choice(df_corse.index, 4, replace=False)
indici_km = random.choice(df_corse.index, 4, replace=False)

df_corse.loc[indici_durata, "durata_minuti"] = np.nan
df_corse.loc[indici_km, "km_percorsi"] = np.nan

# Inserimento duplicati
duplicati = df_corse.head(5)
df_corse = pd.concat([df_corse, duplicati], ignore_index=True)

# Stampa le prime 5 righe del dataframe per check
print("DF CORSE")
print(df_corse)


# df_bici — almeno 20 righe:

#     Colonne: id_bici, tipo, citta, anno_acquisto, costo_acquisto

tipi_bici = ["Elettrica", "Classica"]


structure_bici = {
    "id_bici" : range(1, 21),
    "tipo" : random.choice(tipi_bici, 20),
    "citta" : random.choice(citta, 20),
    "anno_acquisto" : random.randint(2018, 2026, 20),
    "costo_acquisto" : random.randint(300, 3000, 20)
}

df_bici = pd.DataFrame(structure_bici)

print("\nDF BICI")
print(df_bici)


# df_utenti — almeno 25 righe:

#     Colonne: id_utente, nome, citta, tipo_abbonamento, data_iscrizione

nomi = [
    "Luca", "Marco", "Giulia", "Anna", "Sara",
    "Paolo", "Davide", "Elena", "Chiara", "Matteo"
]

abbonamenti = ["Standard", "Plus", "Premium"]

structure_utenti = {
    "id_utente" : range(1, 26),
    "nome" : random.choice(nomi, 25),
    "citta" : random.choice(citta, 25),
    "tipo_abbonamento" : random.choice(abbonamenti, 25),
    "data_iscrizione" : random.choice(pd.date_range("2024-01-01", "2024-12-31"), 25)
}

df_utenti = pd.DataFrame(structure_utenti)

print("\nDF UTENTI")
print(df_utenti)

# 6.2 — Pulizia dati

#   - Rimuovi le righe duplicate
#   - durata_minuti NaN → sostituisci con la mediana per città (usa groupby + transform)
#   - km_percorsi NaN → sostituisci con durata_minuti * 0.18
#   - Converti data_corsa da stringa a datetime
#   - Aggiungi colonne: mese (int) e giorno_settimana (es. "Lunedì")
#   - Stampa .info() e .describe() prima e dopo la pulizia

# Prima della pulizia
print("\nINFO prima della pulizia")
print(df_corse.info())
print("\nDESCRIBE prima la pulizia")
print(df_corse.describe())

df_corse = df_corse.drop_duplicates()

df_corse['durata_minuti'] = df_corse['durata_minuti'].fillna(df_corse.groupby('citta')['durata_minuti'].transform("median").round(2))

df_corse['km_percorsi'] = df_corse['km_percorsi'].fillna(round(df_corse['durata_minuti'] * 0.18, 2))

df_corse["data_corsa"] = pd.to_datetime(df_corse["data_corsa"])

df_corse["mese"] = df_corse["data_corsa"].dt.month

giorni_ITA_ENG = {
    "Monday": "Lunedì",
    "Tuesday": "Martedì",
    "Wednesday": "Mercoledì",
    "Thursday": "Giovedì",
    "Friday": "Venerdì",
    "Saturday": "Sabato",
    "Sunday": "Domenica"
}
df_corse["giorno_settimana"] = df_corse["data_corsa"].dt.day_name().map(giorni_ITA_ENG)

print("\nDF CORSE 2.0")
print(df_corse)

# Dopo la pulizia
print("\nINFO dopo la pulizia")
print(df_corse.info())
print("\nDESCRIBE dopo la pulizia")
print(df_corse.describe())


# 6.3 — Apply e colonne derivate

#   - Applica classifica_corsa() con .apply() → colonna tipo_corsa
#   - Calcola velocita_media = km_percorsi / (durata_minuti / 60)
#   - Calcola costo_stimato con .apply():
#       Breve (< 15 min): € 1.50
#       Media (15–45 min): € 2.50 + € 0.10 × (minuti − 15)
#       Lunga (> 45 min): € 5.00 + € 0.08 × (minuti − 45)

df_corse['tipo_corsa'] = df_corse['durata_minuti'].apply(classifica_corsa)

df_corse["velocita_media"] = round(df_corse["km_percorsi"] / (df_corse["durata_minuti"] / 60), 2)

def calcola_costo(minuti):

    if minuti < 15:
        return 1.50

    elif minuti <= 45:
        return round(2.50 + (0.10 * (minuti - 15)), 2)

    else:
        return round(5.00 + (0.08 * (minuti - 45)), 2)

df_corse["costo_stimato"] = df_corse['durata_minuti'].apply(calcola_costo)

print("\nDF CORSE 3.0")
print(df_corse)


# 6.4 — Aggregazioni e merge

# GroupBy :

#   - Per citta: numero corse, durata media, km totali, costo totale
#   - Per fascia_oraria: numero corse e velocità media
#   - Pivot table: indice = citta, colonne = tipo_corsa, valori = numero corse

aggregazioni_citta = df_corse.groupby('citta').agg(
    numero_corse=("id_corsa", "count"),
    durata_media=("durata_minuti", "mean"),
    km_totali=("km_percorsi", "sum"),
    costo_totale=("costo_stimato", "sum")
)

print("\nAGGREGAZIONI CITTÀ")
print(aggregazioni_citta)


aggregazioni_fascia_oraria = df_corse.groupby('fascia_oraria').agg(
    numero_corse = ("id_corsa", "count"),
    velocita_media = ("velocita_media", "mean")
)

print("\nAGGREGAZIONI FASCIA ORARIA")
print(aggregazioni_fascia_oraria)


pivot_table = df_corse.pivot_table(index = "citta", columns = "tipo_corsa", values = "id_corsa", aggfunc="count")

print("\nPIVOT TABLE")
print(pivot_table)


# Merge :

#   - Unisci df_corse + df_bici su id_bici, poi + df_utenti su id_utente
#   - Stampa le prime 5 righe e le colonne disponibili

df_prima_parte = pd.merge(df_corse, df_bici, on = "id_bici", suffixes=("_corse", "_bici"))
df_completo = pd.merge(df_prima_parte, df_utenti, on = "id_utente", suffixes=("", "_utente"))

df_completo = df_completo.rename(columns={"citta": "citta_utente"})

print("\nDF COMPLETO")
print(df_completo.head(5))


# Top-N :

#   - Le 5 biciclette con più corse
#   - I 3 utenti Premium con costo totale più alto
#   - Aggiungi altre statistiche a piacere

top_corse_bici = df_completo['id_bici'].value_counts().head(5)

print("\nTOP CORSE BICI")
print(top_corse_bici)

top_utenti_premiun = df_completo[df_completo["tipo_abbonamento"] == "Premium"].groupby(["id_utente", "nome"]).agg(costo_totale=("costo_stimato", "sum")).sort_values(by="costo_totale", ascending=False).head(3)

print("\nTOP UTENTI PREMIUM")
print(top_utenti_premiun)

top_fascia_oraria = top_fascia_oraria = df_completo["fascia_oraria"].value_counts().head(3)

print("\nTOP FASCIA ORARIA")
print(top_fascia_oraria)
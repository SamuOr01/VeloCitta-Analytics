# Task 5 — Analisi Numerica con NumPy

from Utility import stampa_riepilogo_analisi

import numpy as np

#     5.1 — Generazione dati

# Usa np.random.seed(42), poi crea:

#    - durate — 500 valori interi da distribuzione normale (media 28, std 12); clippa a ≥ 1
#    - km — durate * np.random.uniform(0.15, 0.25, size=500), arrotondati a 2 decimali
#    - velocita — km / (durate / 60)

# Stampa: shape, dtype e un riepilogo (min, max, media, std) per le tre variabili.

np.random.seed(42)

durate = np.random.normal(loc = 28, scale = 12, size = 500)
durate = durate.clip(min=1)
durate = durate.astype(int)

km = durate * np.random.uniform(low = 0.15, high = 0.25, size = 500)
km = km.round(2)

velocita = np.divide(km, (durate / 60))

stampa_riepilogo_analisi(durate, "durate")
stampa_riepilogo_analisi(km, "km")
stampa_riepilogo_analisi(velocita, "velocita")


#     5.2 — Slicing e selezione

#     - Estrai le prime 10 e le ultime 10 corse (da durate)
#     - Usa fancy indexing per selezionare le corse agli indici [0, 42, 99, 150, 200, 350, 499]
#     - Usa una maschera booleana per trovare le corse con durate > 45 e la loro distanza media
#     - Trova l'indice della corsa con velocità massima e minima

print(f"\nLe prime 10 corse sono: {durate[:10]}")
print(f"\nLe ultime 10 corse sono:{durate[-10:]}")

indici = [0, 42, 99, 150, 200, 350, 499]

print(f"\nLe corse nelle posizioni {indici} sono: {durate[indici]}")
print(f"\nLe corse durate più di 45 minuti sono: {durate[durate > 45]} e la loro distanza media è: {km[durate > 45].mean()}")
print(f"\nL'indice del valore massimo della velocità è: {velocita.argmax()}")
print(f"\nL'indice del valore minimo della velocità è: {velocita.argmin()}")


#     5.3 — Statistiche e normalizzazione

#     - Calcola i percentili 25°, 50°, 75°, 90° delle durate
#     - Normalizza durate con min-max: (x - min) / (max - min); verifica che i valori siano in [0, 1]
#     - Calcola la correlazione di Pearson tra durate e km solo con NumPy; commenta il risultato in una riga

posizioni = [25, 50, 75, 90]

percentili = np.percentile(durate, posizioni)

print(f"\n\nLe percentili delle posizioni {posizioni} sono: {percentili}")

durate_norm = np.divide((durate - durate.min()), (durate.max() - durate.min()))

if durate_norm.min() >= 0 and durate_norm.max() <= 1:
    print(f"\nLe durate sono state normalizzate: [{durate_norm.min()}, {durate_norm.max()}]")

corr_pearson_durate_km = np.corrcoef(durate, km)[0, 1]
print(f"\nLa correlazione di Pearson tra durate e km è: {corr_pearson_durate_km}")
# La correlazione è positiva perché km cresce con la durata.


#     5.4 — Serie temporale simulata

#     - Genera 30 giorni di corse: np.random.randint(80, 200, size=30)
#     - Calcola la media mobile a 7 giorni
#     - Individua il giorno con picco massimo e minimo
#     - Stampa un riepilogo tabellare: giorno, corse, media mobile

giorni = np.random.randint(80, 200, size=30)

print(f"\n\nI 30 giorni di corse sono: {giorni}")

finestra_temporale = 7
scorrimento_finestra = np.ones(finestra_temporale) / finestra_temporale
media_mobile = np.convolve(giorni, scorrimento_finestra, mode = "valid")

print(f"\nLa media mobile a 7 giorni è: {media_mobile}")

picco_massimo = giorni.argmax() + 1
picco_minimo = giorni.argmin() + 1

print(f"\nIl giorno con il Picco Massimo è: {picco_massimo} con {giorni.max()}")
print(f"\nIl giorno con il Picco Minimo è: {picco_minimo} con {giorni.min()}")

print("\n Giorno | Corse | Media mobile (7gg)")

for i in range(len(giorni)):

    if i >= finestra_temporale - 1:
        print(f" {i+1:6} | {giorni[i]:5} | {media_mobile[i - (finestra_temporale - 1)]}")
    else:
        print(f" {i+1:6} | {giorni[i]:5} | {"---":>10}")
# Task 7 — Visualizzazione

#   - Ogni grafico deve avere: titolo, etichette assi, legenda (dove necessaria).
#   - Aggiungi un commento nel codice (1-2 righe) con la domanda di business a cui risponde.
#   - Deve essere salvato come png in una cartella apposita della repo

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Pandas import df_completo, df_corse, df_bici, df_utenti

# Grafico 1 — Serie temporale corse → output/01_serie_temporale.png

#   - Matplotlib, line plot
#   - Una linea per città, colori distinti
#   - Usa plt.rcParams per almeno una personalizzazione globale

# Creo un DataFrame raggruppato per data e città
df_serie_temporale = df_corse.groupby(["data_corsa", "citta"]).size().unstack().fillna(0)

# Dimensione grafico globale
plt.rcParams["figure.figsize"] = (12, 6)

# Dimensione titolo assi
plt.rcParams["axes.titlesize"] = 14

# Spessore linee
plt.rcParams["lines.linewidth"] = 2



# Crea nuova figura
plt.figure()

# Ciclo per ogni città
for col in df_serie_temporale.columns:

    # Crea le linee delle città
    plt.plot(df_serie_temporale.index, df_serie_temporale[col], label = col)

# Titolo grafico
plt.title("Serie temporale corse per città")

# Etichetta asse X
plt.xlabel("Data")

# Etichetta asse Y
plt.ylabel("Numero corse")

# Legenda
plt.legend(title = "Città")

# Layout automatico
plt.tight_layout()

# Salva il grafico nella cartella output
plt.savefig("VeloCitta-Analytics/output/01_serie_temporale.png")

# Mostra il grafico
plt.show()

# Domanda business: come variano nel tempo le corse nelle diverse città?
# Serve per capire stagionalità e distribuzione geografica della domanda.


# Grafico 2 — Distribuzione durate per città → output/02_distribuzione_durate.png

#   - Seaborn histplot con KDE
#   - hue = città, tema whitegrid

# Dimensione figura
plt.figure(figsize = (10, 6))

# Tema seaborn
sns.set_style("whitegrid")

# Grafico
graph = sns.histplot(

    # DataFrame
    data = df_corse,

    # Asse X
    x = "durata_minuti",

    # Colore per città
    hue = "citta",

    # Curva di densità dell"intervallo
    kde = True,

    # Numero di “contenitori” in cui sono raggruppati i dati.
    bins = 20,

    # Trasparenza
    alpha = 0.5
)

# Titolo grafico
graph.set_title("Distribuzione durate corse per città")

# Etichetta asse X
graph.set_xlabel("Durata (minuti)")

# Etichetta asse Y
graph.set_ylabel("Numero corse")

# Legenda
graph.legend(title = "Città")

# Layout automatico
plt.tight_layout()

# Salva il grafico nella cartella output
plt.savefig("VeloCitta-Analytics/output/02_distribuzione_durate.png")

# Mostra il grafico
plt.show()

# Domanda business: come si distribuiscono le durate delle corse nelle diverse città?
# Serve per capire differenze di comportamento tra utenti nelle varie aree.


# Grafico 3 — Corse per fascia oraria e tipo → output/03_fasce_orarie.png

#   - Seaborn barplot
#   - Barre raggruppate per tipo bicicletta (classica / elettrica)

# DataFrame per conta le corse
df_fasce_orarie_corse = df_completo.groupby(["fascia_oraria", "tipo"])["id_corsa"].count().reset_index(name = "id_corsa")

# Dimensione figura
plt.figure(figsize = (10, 6))

# Tema seaborn
sns.set_style("whitegrid")

graph = sns.barplot(

    # DataFrame
    data = df_fasce_orarie_corse,

    # Asse X
    x = "fascia_oraria",

    # Asse Y
    y = "id_corsa",

    # Barre per tipo bici
    hue = "tipo"
)

# Titolo
graph.set_title("Corse per fascia oraria e tipo di bicicletta")

# Etichetta X
graph.set_xlabel("Fascia oraria")

# Etichetta Y
graph.set_ylabel("Numero di corse")

# Legenda
graph.legend(title = "Tipo")

# Layout automatico
plt.tight_layout()

# Salva il grafico nella cartella output
plt.savefig("VeloCitta-Analytics/output/03_fasce_orarie.png")

# Mostra il grafico
plt.show()

# Domanda di business: quali fasce orarie sono più utilizzate e come varia l’uso tra bici classiche ed elettriche?


# Grafico 4 — Scatter durata vs. velocità → output/04_scatter_durata_velocita.png

#   - Matplotlib scatter, colore punti per città
#   - Linea di tendenza con np.polyfit

# Dimensione figura
plt.figure(figsize = (10, 6))

# Colori per il grafico delle città
colors = {
    "Milano": "blue",
    "Roma": "green",
    "Torino": "red"
}

# Ciclo per ogni città
for citta, color in colors.items():

    # Filtra città
    subset = df_corse[df_corse["citta"] == citta]

    plt.scatter(

        # Asse X
        subset["durata_minuti"],

        # Asse Y
        subset["velocita_media"],

        # Legenda
        label = citta,

        # Trasparenza punti
        alpha = 0.6,

        # Colore punti
        color = color
    )

# Linea di tendenza globale
x = df_corse["durata_minuti"]
y = df_corse["velocita_media"]

# Rimuove NaN
mask = x.notna() & y.notna()

# Fit lineare
m, b = np.polyfit(x[mask], y[mask], 1)

# Disegna linea
plt.plot(
    x,
    m * x + b,
    color = "black",
    linewidth = 2,
    label = "Trend line"
)

# Titolo
plt.title("Scatter Durata VS Velocità")

# Asse X
plt.xlabel("Durata (minuti)")

# Asse Y
plt.ylabel("Velocità media (km/h)")

# Legenda
plt.legend(title = "Città")

# Layout automatico
plt.tight_layout()

# Salva il grafico nella cartella output
plt.savefig("VeloCitta-Analytics/output/04_scatter_durata_velocita.png")

# Mostra il grafico
plt.show()

# Domanda di business: esiste una relazione tra durata della corsa e velocità media? Cambia tra le città?


# Grafico 5 — Dashboard riepilogativa → output/05_dashboard.png

#   - plt.subplots(2, 2) con suptitle e tight_layout
#   - In alto sx: bar chart corse per città
#   - In alto dx: pie chart abbonamenti utenti
#   - In basso sx: bar chart costo totale per città
#   - In basso dx: Seaborn boxplot durate per tipo corsa

#     Aggiungete altri grafici a vostra scelta

# Crea 4 contenitori
fig, axes = plt.subplots(2, 2, figsize = (14, 10))

# Titolo globale
fig.suptitle("Dashboard riepilogativa VeloCittà", fontsize = 16)

# 1. In alto sx — corse per città

# Conteggio corse per città
df_citta = df_completo["citta_corse"].value_counts()

# Barre città
axes[0, 0].bar(df_citta.index, df_citta.values, color = ["dodgerblue", "darkorange", "seagreen"])

# Titolo contenitore
axes[0, 0].set_title("Corse per città")

# Etichetta X
axes[0, 0].set_xlabel("Città")
# Etichetta Y
axes[0, 0].set_ylabel("Numero corse")


# 2. In alto dx — abbonamenti utenti (pie)

# Conteggio abbonamenti
df_abbonamenti = df_completo["tipo_abbonamento"].value_counts()

# Grafico a torta
axes[0, 1].pie(
    df_abbonamenti.values,
    labels = df_abbonamenti.index,
    autopct = "%1.1f%%",
    startangle = 90
)

# Titolo
axes[0, 1].set_title("Tipi di abbonamento")


# 3. In basso sx — costo totale per città

# Costo totale città
df_costo_citta = df_completo.groupby("citta_corse")["costo_stimato"].sum()

# Barre costo
axes[1, 0].bar(
    df_costo_citta.index,
    df_costo_citta.values,
    color = ["tomato", "violet", "yellow"]
)

# Titolo contenitore
axes[1, 0].set_title("Costo totale per città")

# Etichetta X
axes[1, 0].set_xlabel("Città")

# Etichetta Y
axes[1, 0].set_ylabel("€")


# 4. In basso dx — boxplot durate per tipo corsa

# Creazione grafico
sns.boxplot(
    data = df_completo,
    x = "tipo_corsa",
    y = "durata_minuti",
    ax = axes[1, 1],
    palette = ["coral", "royalblue", "darkviolet"]
)

# Titolo contenitore
axes[1, 1].set_title("Durata corse per tipo")


# Layout finale
plt.tight_layout(rect = [0, 0, 1, 0.95])

# Salva il grafico nella cartella output
plt.savefig("VeloCitta-Analytics/output/05_dashboard.png")

# Mostra il grafico
plt.show()
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

# df_serie_temporale = df_corse.groupby(["data_corsa", "citta"]).size().unstack().fillna(0)

# plt.rcParams["figure.figsize"] = (12, 6)
# plt.rcParams["axes.titlesize"] = 14
# plt.rcParams["lines.linewidth"] = 2

# # Domanda business: come variano nel tempo le corse nelle diverse città?
# # Serve per capire stagionalità e distribuzione geografica della domanda.

# plt.figure()

# for col in df_serie_temporale.columns:
#     plt.plot(df_serie_temporale.index, df_serie_temporale[col], label = col)

# plt.title("Serie temporale corse per città")
# plt.xlabel("Data")
# plt.ylabel("Numero corse")
# plt.legend(title = 'Città')

# plt.tight_layout()

# plt.savefig("VeloCitta-Analytics/output/01_serie_temporale.png")
# plt.show()


# Grafico 2 — Distribuzione durate per città → output/02_distribuzione_durate.png

#   - Seaborn histplot con KDE
#   - hue = città, tema whitegrid

# Domanda business: come si distribuiscono le durate delle corse nelle diverse città?
# Serve per capire differenze di comportamento tra utenti nelle varie aree.

# plt.figure(figsize = (10, 6))
# sns.set_style("whitegrid")

# graph = sns.histplot(
#     data = df_corse,
#     x = "durata_minuti",
#     hue = "citta",
#     kde = True,
#     bins = 20,
#     alpha = 0.5
# )

# graph.set_title("Distribuzione durate corse per città")
# graph.set_xlabel("Durata (minuti)")
# graph.set_ylabel("Numero corse")
# graph.legend(title = "Città")

# plt.tight_layout()

# plt.savefig("VeloCitta-Analytics/output/02_distribuzione_durate.png")
# plt.show()


# Grafico 3 — Corse per fascia oraria e tipo → output/03_fasce_orarie.png

#   - Seaborn barplot
#   - Barre raggruppate per tipo bicicletta (classica / elettrica)

# df_fasce_orarie_corse = df_completo.groupby(["fascia_oraria", "tipo"])["id_corsa"].count().reset_index(name = "id_corsa")

# # Domanda di business: quali fasce orarie sono più utilizzate e come varia l’uso tra bici classiche ed elettriche?

# plt.figure(figsize = (10, 6))
# sns.set_style("whitegrid")

# graph = sns.barplot(
#     data = df_fasce_orarie_corse,
#     x = "fascia_oraria",
#     y = "id_corsa",
#     hue = "tipo"
# )

# graph.set_title("Corse per fascia oraria e tipo di bicicletta")
# graph.set_xlabel("Fascia oraria")
# graph.set_ylabel("Numero di corse")
# graph.legend(title = "Tipo")

# plt.tight_layout()
# plt.savefig("VeloCitta-Analytics/output/03_fasce_orarie.png")
# plt.show()


# Grafico 4 — Scatter durata vs. velocità → output/04_scatter_durata_velocita.png

#   - Matplotlib scatter, colore punti per città
#   - Linea di tendenza con np.polyfit

# Domanda di business: esiste una relazione tra durata della corsa e velocità media? Cambia tra le città?

# plt.figure(figsize = (10, 6))

# colors = {
#     "Milano": "blue",
#     "Roma": "green",
#     "Torino": "red"
# }

# for citta, color in colors.items():
#     subset = df_corse[df_corse["citta"] = =  citta]

#     plt.scatter(
#         subset["durata_minuti"],
#         subset["velocita_media"],
#         label = citta,
#         alpha = 0.6,
#         color = color
#     )

# # Linea di tendenza globale
# x = df_corse["durata_minuti"]
# y = df_corse["velocita_media"]

# mask = x.notna() & y.notna()

# m, b = np.polyfit(x[mask], y[mask], 1)

# plt.plot(
#     x,
#     m * x + b,
#     color = "black",
#     linewidth = 2,
#     label = "Trend line"
# )

# plt.title("Scatter Durata VS Velocità")
# plt.xlabel("Durata (minuti)")
# plt.ylabel("Velocità media (km/h)")
# plt.legend()

# plt.tight_layout()
# plt.savefig("VeloCitta-Analytics/output/04_scatter_durata_velocita.png")
# plt.show()


# Grafico 5 — Dashboard riepilogativa → output/05_dashboard.png

#   - plt.subplots(2, 2) con suptitle e tight_layout
#   - In alto sx: bar chart corse per città
#   - In alto dx: pie chart abbonamenti utenti
#   - In basso sx: bar chart costo totale per città
#   - In basso dx: Seaborn boxplot durate per tipo corsa

#     Aggiungete altri grafici a vostra scelta

fig, axes = plt.subplots(2, 2, figsize = (14, 10))

fig.suptitle("Dashboard riepilogativa VeloCittà", fontsize = 16)

# -------------------------------------------------
# 1. In alto sx — corse per città
# -------------------------------------------------
df_citta = df_completo["citta_corse"].value_counts()

axes[0, 0].bar(df_citta.index, df_citta.values, color = ["dodgerblue", "darkorange", "seagreen"])
axes[0, 0].set_title("Corse per città")
axes[0, 0].set_xlabel("Città")
axes[0, 0].set_ylabel("Numero corse")

# -------------------------------------------------
# 2. In alto dx — abbonamenti utenti (pie)
# -------------------------------------------------
df_abbonamenti = df_completo["tipo_abbonamento"].value_counts()

axes[0, 1].pie(
    df_abbonamenti.values,
    labels = df_abbonamenti.index,
    autopct = "%1.1f%%",
    startangle = 90
)

axes[0, 1].set_title("Tipi di abbonamento")

# -------------------------------------------------
# 3. In basso sx — costo totale per città
# -------------------------------------------------
df_costo_citta = df_completo.groupby("citta_corse")["costo_stimato"].sum()

axes[1, 0].bar(
    df_costo_citta.index,
    df_costo_citta.values,
    color = ["tomato", "violet", "yellow"]
)

axes[1, 0].set_title("Costo totale per città")
axes[1, 0].set_xlabel("Città")
axes[1, 0].set_ylabel("€")

# -------------------------------------------------
# 4. In basso dx — boxplot durate per tipo corsa
# -------------------------------------------------
sns.boxplot(
    data = df_completo,
    x = "tipo_corsa",
    y = "durata_minuti",
    ax = axes[1, 1],
    palette = ["coral", "royalblue", "darkviolet"]
)

axes[1, 1].set_title("Durata corse per tipo")

# -------------------------------------------------
# Layout finale
# -------------------------------------------------
plt.tight_layout(rect = [0, 0, 1, 0.95])
plt.savefig("VeloCitta-Analytics/output/05_dashboard.png")
plt.show()
# VeloCitta-Analytics

Autore: Orefice Samuele -- samu.or01@gmail.com

## Descrizione
Progetto di analisi dati per la startup italiana di bike sharing VeloCittà attiva a Milano, Roma e Torino. Il progetto unisce simulazione dei dati, pulizia, analisi statistica e visualizzazione dei grafici per ottenere insight sui pattern di utilizzo, differenze tra città e fasce orarie. Include anche esercizi di OOP e query SQL teoriche per comprendere meglio la gestione della flotta e dei dati.

## Installazione
Per prima cosa è necessario installare i requisiti attravero il comando:
```bash
pip install -r requirements.txt
```
Successivamente eseguire gli script nel seguente ordine:

    1) OOP.py
    2) Analisi_Numpy.py
    3) Pandas.py
    4) Visualizzazione.py
 
>[!NOTE]
>- Il file QuerySQL.sql contiene solamente la spiegazione teorica sull'interrogazione di ipotetiche tabelle.  
>- Il Utility.py contiene solamente delle funzioni di utilità che vengono richiamate dagli altri script

## Considerazioni
Durante lo sviluppo del progetto, ho trovato particolarmente sfidante soddisfare tutte le task relative alla libreria Pandas, in particolare la pulizia dei dati, il calcolo delle colonne derivate e l’integrazione dei diversi DataFrame con i grafici. Migliorerei la generazione dei dati simulati aggiungendo variabili come condizioni meteo o traffico, così da rendere l’analisi più realistica e predittiva. Inoltre integrerei l'utilizzo di un database SQL vero e proprio per l'immagazzinamento dei dati.
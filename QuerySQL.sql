/*
Solo query SQL e spiegazioni testuali. Nessun codice Python.

Tabelle disponibili:

- corse(id_corsa, id_bici, id_utente, stazione_partenza, stazione_arrivo,
      data_corsa, durata_minuti, km_percorsi)

- biciclette(id_bici, tipo, citta, stazione_corrente, km_totali)

- utenti(id_utente, nome, citta, tipo_abbonamento, data_iscrizione)

- stazioni(id_stazione, nome, citta, n_posti, latitudine, longitudine)

Per ogni domanda scrivi: la query SQL + una spiegazione di 1-3 righe.
*/

/*
    D1 — Tutte le corse a Milano ordinate per data decrescente.
    Mostra: id_corsa, id_bici, data_corsa, durata_minuti.
*/
	# Mostra id_corsa, id_bici, data_corsa, durata_minuti
    SELECT
		corse.id_corsa,
        corse.id_bici,
        corse.data_corsa,
        corse.durata_minuti
    # Dalla tabella corse
    FROM corse
    # Usa due join separati sulla tabella corse per ottenere città di partenza e arrivo
	INNER JOIN stazioni sp ON corse.stazione_partenza = sp.nome
	INNER JOIN stazioni sa ON corse.stazione_arrivo = sa.nome
    # Solo le corse in cui la città della stazione di partenza oppure la città della
    # stazione di arrivo è “Milano”
	WHERE sp.citta = 'Milano'
	   OR sa.citta = 'Milano'
    # Ordinati per data decrescente
    ORDER BY corse.data_corsa DESC;

/*
    Spiegazione: Questa query restituisce tutte le corse che hanno come punto
    di partenza o arrivo Milano,ordinandole dalla più recente alla più vecchia.
    Serve a monitorare le corse nella città.
*/


/*
    D2 — Quante bici elettriche per ogni città?
    Ordina dalla città con più bici a quella con meno.
*/
	# Mostra le città e conta tutte le bici
    SELECT biciclette.citta, COUNT(*)
    # Dalla tabella biciclette
    FROM biciclette
    # Mostra solo quelle elettriche
    WHERE biciclette.tipo = "elettrica"
    GROUP BY biciclette.citta
    # In ordine decrescente
    ORDER BY COUNT(*) DESC;

/*
    Spiegazione: Conta quante bici elettriche ci sono in ogni città,
    utile per capire la distribuzione della flotta. Le città con più
    bici elettriche appaiono per prime.
*/


/*
    D3 — Durata media, massima e minima per tipo di bicicletta.
    (JOIN richiesto)
*/
	# Mostra durata media, massima e minima
    SELECT
		biciclette.tipo,
		AVG(corse.durata_minuti) as Durata_Media,
        MAX(corse.durata_minuti) as Durata_Massima,
        MIN(corse.durata_minuti) as Durata_Minima
	# Dalla tabella corse
	FROM corse
    # Per le bici in comune nella tabella biciclette
    INNER JOIN biciclette
		ON corse.id_bici = biciclette.id_bici
	# Ordinate per tipo bicicletta
	GROUP BY biciclette.tipo;

/*
    Spiegazione: Calcola statistiche di durata delle corse raggruppate
    per tipo di bicicletta. Permette di confrontare l'utilizzo tra bici
    classiche ed elettriche.
*/


/*
    D4 — Stazioni di Milano con più di 50 arrivi in aprile 2026.
    Ordina per conteggio decrescente.
*/

	SELECT stazioni.nome, COUNT(corse.id_corsa)
    FROM stazioni
    INNER JOIN corse
		ON stazioni.nome = corse.stazione_arrivo
    WHERE stazioni.citta = "Milano"
        AND corse.data_corsa BETWEEN '2026-04-01' AND '2026-04-30'
	GROUP BY stazioni.nome
	HAVING COUNT(corse.id_corsa) > 50
	ORDER BY COUNT(corse.id_corsa) DESC;

/*
    Spiegazione: Mostra le stazioni milanesi più frequentate ad
    aprile 2026. Filtra solo quelle con oltre 50 arrivi e le ordina
    partendo dalla più trafficata.
*/


/*
    D5 — Utenti "Premium" con almeno 10 corse: mostra numero corse totali e km totali.
    (JOIN richiesto)
*/

	SELECT
		utenti.id_utente,
		utenti.nome,
        COUNT(corse.id_corsa) AS totale_corse,
        SUM(corse.km_percorsi) AS km_totali
    FROM utenti
    INNER JOIN corse
		ON utenti.id_utente = corse.id_utente
	WHERE utenti.tipo_abbonamento = 'Premium'
	GROUP BY utenti.id_utente, utenti.nome
	HAVING COUNT(corse.id_corsa) >= 10;

/*
    Spiegazione: Evidenzia gli utenti Premium più attivi,
    mostrando quante corse hanno fatto e quanti km hanno percorso.
*/


/*
    D6 — Spiega a parole cosa fa questa query e quale informazione di business produce:
*/

	# Mostra nome, città delle stazioni, conta gli arrivi e le partenze,
    # mostra il bilancio tra arrivi e partenze
    SELECT
        s.nome AS stazione,
        s.citta,
        COUNT(c_in.id_corsa)  AS arrivi,
        COUNT(c_out.id_corsa) AS partenze,
        COUNT(c_in.id_corsa) - COUNT(c_out.id_corsa) AS bilancio
	# Dalla tabella stazioni
    FROM stazioni s
    # Usa due join separati sulla tabella corse per contare
    # le corse in arrivo e in partenza dalla stazione
    LEFT JOIN corse c_in  ON s.nome = c_in.stazione_arrivo
    LEFT JOIN corse c_out ON s.nome = c_out.stazione_partenza
    # Raggruppati per nome e città delle stazioni
    GROUP BY s.nome, s.citta
    # Con bilancio in ordine descrescente
    ORDER BY bilancio DESC;

/*
    Spiegazione: La query calcola per ogni stazione il numero di
    arrivi e partenze,mostrando anche il "bilancio" (arrivi meno partenze).
    Serve a identificare stazioniche accumulano bici o che invece ne perdono
*/
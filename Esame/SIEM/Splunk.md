## SIEM (Security Information and Event Management)

Piattaforma di log management e analisi dei dati macchina.
Usato per raccogliere log eterogenei (Linux audit, Apache access, Windows Event Log,...), vengono centralizzati, indicizzati e indicizzati e resi interrogabili in tempo quasi reale per detection, threat hunting e incident response.

Logica di base:
- Raccogli i log;
- Indicizza;
- Cerca;
- Visualizza/Alerta;

## Architettura

- Forwarder: Agente installato sulle macchine sorgente che spedisce i log;
- Indexer: Riceve i log, fa parsing, indicizza e salva i dati su disco;
- Search Head: interfaccia web dove scrivi query SPL e costruisci dashboard/report/aler;

## Modello dati: come Splunk organizza gli eventi

Ogni evento viene taggato con alcuni metadati chiave:
- Index;
- Sourcetype: tipo di dato, definisce come va parsato;
- Source: file/percorso originale;
- Host: macchina di provenienza;
- \_time: timestamp;

## SPL (Search Processing Language)

Struttura a pipeline in sile Unix: ogni ```|``` passa i risultati al comando successivo.

```
	index="..." filtro_iniziale | comando1 | comando2 | ...
```



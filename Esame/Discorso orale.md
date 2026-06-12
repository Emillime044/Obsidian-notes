**1. Titolo (~15s)**

- Saluti, nome, una riga: "lavoro di stage, portare la ISO 27001 dalla teoria alla pratica operativa in una PMI."

**2. Digital74 (~35s)**

- PMI di Verona, servizi IT e WebApp, cliente principale AICA.
- Già ISO 9001, **in fase** di certificazione 27001 → qui entra il mio lavoro.
- Calca su "è piccola": è il filo rosso di tutto.

**3. Obiettivi (~30s)**

- Tradurre lo standard in procedure concrete; completare la doc lato operativo; **calibrare il dettaglio senza sovra-ingegnerizzare.**
- Sottolinea il terzo: è la sfida vera in una PMI.

**4. Cos'è un SGSI (~50s)**

- Frase secca: "insieme strutturato di policy, procedure e responsabilità per gestire la sicurezza delle informazioni."
- Si basa sull'**analisi del rischio**; punta a riservatezza-integrità-disponibilità ([[Cifratura Asimmetrica#Triade CIA|CIA]]); logica di miglioramento continuo.
- Ponte: "si basa sull'analisi del rischio — ed è esattamente da lì che parto."

**5. La base del sistema / matrice (~55s)**

- "La matrice incrocia asset, minacce, probabilità e impatto per capire cosa è davvero prioritario."
- **Percorri UNA riga davanti a loro**: "Database di produzione → probabilità 3, impatto 5 → rischio 15, critico → contromisura backup immutabile + EDR + segmentazione → playbook D-RW-01."
- Messaggio: tracciabilità rischio→risposta, e **da qui escono i 7 scenari.**

**6. Il progetto principale / 7 scenari (~45s)**

- "Dai rischi critici della matrice sono usciti 7 scenari." Ne citi 2-3 d'impatto: ransomware, account admin, disastro fisico.
- **Ponte verbale:** "Per ognuno ho scritto un playbook. Ma cos'è, esattamente, un playbook?"

**7. A cosa serve un playbook (~35s)**

- Frase che fa colpo: "serve a decidere a freddo ed eseguire sotto pressione."
- Cosa fare, chi, in che ordine → riduce gli errori da stress.

**8. Come è fatto (~55s)**

- Scorri le 4 sezioni, una frase ciascuna: Inquadramento / Struttura (asset, RTO-RPO, severità) / Ruoli (RACI) / Esecuzione (le 5 fasi).
- RTO/RPO e RACI li lasci promessi: "li vediamo concretamente ora."

**9. Caso concreto Ransomware (~70s) — rallenta, è il pezzo clou**

- Isolare **non** spegnere → spegnere cancella la RAM (prove + chiavi).
- Nessun pagamento del riscatto.
- Eradicazione = formattazione e reinstallazione, non "ripulire".
- RTO: 4h database, 8h sistemi critici, 24–48h il resto (a voce).
- **RPO = ultimo backup verificato come integro**: col ransomware non conta l'ultimo backup, conta l'ultimo backup _sano_.

**10. Matrice RACI (~45s)**

- Incornicia come continuazione: "e per quello stesso incidente, ecco chi fa cosa."
- "Quattro ruoli: chi esegue, chi ne risponde, chi consulti, chi informi."
- **Percorri una riga**, es. "Notifiche alle autorità" (apre al GDPR se chiedono).
- Taglio PMI: una persona ricopre più ruoli → metterlo nero su bianco evita il "pensavo lo facessi tu".

**11. Difficoltà (~35s)**

- Calibrare il dettaglio (il tema ricorrente); D-AI-07 con vincoli esterni e colleghi del test center; rischi sfumati gestiti con **criteri documentati**.
- Tono maturo, non lamentela.

**12. Risultati e competenze (~35s)**

- A coppie, veloce: 7 playbook + traduzione normativa; matrice aggiornata + autonomia; policy integrate + scrittura tecnico-normativa.

**13. Sviluppi futuri (~30s)**

- Tabletop exercise; test a regime (restore mensile, failover cloud annuale); integrazione SGSI–ISO 9001 senza duplicare.
- Dimostra che pensi al ciclo di vita.

**14. Grazie (~10s)**

- Ringrazi, ti rendi disponibile alle domande.
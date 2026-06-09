**Slide 1 — Titolo (~25s)**

"Buongiorno, sono Emil Simonetti. Vi presento il lavoro che ho svolto durante lo stage in Digital74: la stesura di una serie di playbook operativi per portare l'azienda verso la conformità alla ISO 27001, all'interno del suo Sistema di Gestione della Sicurezza delle Informazioni."

_(Pausa, vai avanti.)_

---

**Slide 2 — Digital74 (~45s)**

"Due parole sull'azienda, perché il contesto conta. Digital74 è una PMI di Verona, una realtà di nove persone, che si occupa di servizi IT e di progettazione e gestione di web application. Il cliente principale è AICA, l'ente per le certificazioni informatiche, e questo dettaglio tornerà più avanti perché ha pesato su uno degli scenari che ho dovuto gestire. L'azienda è già certificata ISO 9001 per la gestione della qualità, ed è in fase di certificazione ISO 27001. Ed è qui che si inserisce il mio lavoro."

---

**Slide 3 — Obiettivi dello stage (~45s)**

"Gli obiettivi erano tre, ed erano molto concreti. Primo: tradurre lo standard ISO 27001 — che è un testo normativo, astratto — in procedure operative che una persona possa effettivamente seguire. Secondo: completare la documentazione del Sistema di Gestione dal lato operativo, perché la parte di governance c'era già ma mancava il 'cosa si fa nel momento dell'incidente'. Terzo, e forse il più delicato: calibrare il livello di dettaglio per una PMI. Cioè non sovra-ingegnerizzare. Una procedura pensata per una multinazionale, in un'azienda di nove persone, semplicemente non viene usata."

---

**Slide 4 — Cos'è un SGSI (~50s)**

"Faccio un passo indietro per chi non mastica la terminologia. SGSI sta per Sistema di Gestione della Sicurezza delle Informazioni. In pratica è un insieme strutturato di policy, procedure e responsabilità, costruito a partire dall'analisi del rischio. L'obiettivo è proteggere tre proprietà delle informazioni: riservatezza, integrità e disponibilità — quella che in gergo chiamiamo la triade CIA. E la cosa importante è che non è un documento che scrivi una volta e archivi: è un sistema basato sul miglioramento continuo, che si aggiorna man mano che cambiano i rischi e l'azienda."

---

**Slide 5 — Il progetto principale (~60s)**

"Il cuore del mio lavoro è stato questo: scrivere sette playbook di disaster recovery, uno per ciascuno dei sette scenari che erano stati valutati come più rischiosi nella matrice dei rischi aziendale. Li trovate elencati: si va dal ransomware, alla perdita o corruzione del database, all'indisponibilità del cloud, fino a un account amministrativo compromesso, alla perdita del repository Git, a un disastro fisico in sede, e infine all'interruzione del test center AICA. Ogni codice — D-RW-01, D-DB-02 e così via — identifica un playbook specifico. Non sono scenari scelti a caso: derivano direttamente dalla valutazione del rischio, quindi rispondono a minacce reali per quella azienda."

---

**Slide 6 — A cosa serve un playbook (~45s)**

"Ma cos'è di preciso un playbook? È un documento operativo che risponde a tre domande durante un incidente: cosa fare, chi lo fa, e in che ordine. Il motivo per cui esiste è semplice: durante un incidente le persone sono sotto stress, e sotto stress si fanno errori. Il playbook serve proprio a questo — ridurre gli errori, dare linee guida precise. L'idea di fondo, che secondo me è la chiave di tutto, è: decidere a freddo, eseguire sotto pressione. Le decisioni difficili le prendi prima, quando hai la testa lucida. Nel momento dell'incidente segui quello che hai già deciso."

---

**Slide 7 — Come è fatto un playbook (~60s)**

"Strutturalmente ogni playbook segue lo stesso schema, ed è organizzato in quattro blocchi. Il primo è l'inquadramento: scopo, ambito, scenario di riferimento e riferimenti normativi. Il secondo è la struttura tecnica: quali asset e servizi sono coinvolti, gli RTO e RPO — cioè i tempi e i punti di ripristino obiettivo — e i trigger con i livelli di severità che fanno scattare il playbook. Il terzo blocco sono ruoli e responsabilità: chi è l'incident manager, chi i referenti, e una matrice RACI che assegna i compiti. Il quarto è l'esecuzione vera e propria, la sequenza di azioni. Avere uno schema fisso non è un dettaglio estetico: significa che chi apre un playbook qualsiasi sa già dove trovare l'informazione che cerca."

---

**Slide 8 — Caso concreto: Ransomware (~75s — questa è centrale, prenditi il tempo)**

"Vi faccio vedere un caso concreto, il D-RW-01, lo scenario ransomware, che è quello su cui ho lavorato più a fondo. Qui ci sono alcune scelte operative che vale la pena spiegare. Prima: in caso di infezione, si isola la macchina, ma non si spegne. Sembra controintuitivo, ma spegnere la macchina cancella la RAM, e nella RAM possono esserci informazioni utili per l'analisi forense, a volte addirittura chiavi di cifratura. Seconda scelta, netta: nessun pagamento del riscatto. È una posizione presa a monte, non una decisione da prendere nel panico del momento. Terza: l'eradicazione della minaccia avviene con format e reinstallazione completa — non ci si fida di una pulizia parziale. Sui tempi, l'RTO è di otto ore per i sistemi critici e ventiquattro per le postazioni di lavoro. E qui c'è un punto che tengo a sottolineare: l'RPO effettivo non è il backup più recente, ma l'ultimo backup verificato come integro. Perché un backup cifrato dal ransomware è inutile. È una distinzione che cambia completamente la strategia di ripristino."

---

**Slide 9 — La matrice RACI (~50s)**

"Questa è la matrice RACI dello scenario ransomware. RACI sta per Responsible, Accountable, Consulted, Informed: per ogni attività definisce chi la esegue, chi ne risponde, chi va consultato e chi solo informato. Se guardate la tabella, ogni riga è una fase dell'incidente — rilevazione, contenimento, eradicazione, ripristino, fino alla chiusura e alle lessons learned. Un dettaglio che riflette la realtà di una PMI: vista la dimensione aziendale, una stessa persona può ricoprire più ruoli. In un'azienda di nove persone non hai un team dedicato per ogni funzione, quindi la matrice è stata calibrata su questo, restando comunque chiara su chi ha la responsabilità finale di ciascuna decisione."

---

**Slide 10 — Difficoltà riscontrate (~45s)**

"Le difficoltà principali sono state tre. La prima, quella che ho citato all'inizio: calibrare il livello di dettaglio. Né sovra-ingegnerizzare, né rendere il documento così generico da essere inutile. È un equilibrio che ho aggiustato man mano. La seconda riguarda il D-AI-07, il test center AICA: lì entravano in gioco i vincoli di un soggetto esterno, e ho dovuto coinvolgere direttamente i colleghi del test center per capire come funzionava davvero. La terza: alcuni rischi erano più sfumati, difficili da valutare in modo netto. In quei casi ho documentato esplicitamente i criteri di valutazione nella matrice di risk analysis, così che la scelta fosse tracciabile e non arbitraria."

---

**Slide 11 — Risultati e competenze (~40s)**

"Tirando le somme sui risultati: sette playbook completati, la matrice dei rischi aggiornata, e le policy operative integrate nel Sistema di Gestione. Sul piano delle competenze, questo lavoro mi ha fatto crescere su tre fronti: la traduzione di testo normativo in qualcosa di usabile per una PMI, la scrittura tecnico-normativa, e la gestione autonoma delle priorità — perché molte di queste decisioni le ho prese e documentate in autonomia."

---

**Slide 12 — Sviluppi futuri (~40s)**

"Il lavoro non si chiude qui. I prossimi passi sono tre. Primo: testare i playbook con dei tabletop exercise, cioè simulazioni a tavolino, perché un playbook che non è mai stato provato non sai se funziona davvero. Secondo: test tecnici a regime — un restore mensile a campione per il database, e un failover annuale dei servizi cloud. Terzo: integrare il Sistema di Gestione della Sicurezza con la ISO 9001 già esistente, evitando duplicazioni e sfruttando ciò che l'azienda ha già."
## Penetration Test Report 

**[Nome Progetto / Engagement]**

### Document Control

| Campo           | Valore               |
| --------------- | -------------------- |
| Cliente         | [Nome Cliente]       |
| Autore          | [Nome Tester]        |
| Revisore        | [Nome Revisore]      |
| Versione        | [1.0]                |
| Data            | [Data]               |
| Classificazione | CONFIDENZIALE        |
| Distribuzione   | [Elenco destinatari] |
### Disclaimer / Autorizzazione

Le attività descritte sono state condotte previa autorizzazione esplicita del committente, entro il perimetro concordato e in un intervallo temporale definito. I risultati rappresentano una fotografia dello stato di sicurezza al momento del test e non garantiscono l'assenza di ulteriori vulnerabilità.

---
## Executive Summary
È stato condotto un penetration test in modalità [black-box/gray-box/white-box] su applicazione web sull'infrastruttura di [nomeCliente], raggiungibile dall'url [urlwebapp] e relativi sottodomini.
L'assessment ha coperto [autenticazione/autorizzazione/validazione degli input/sicurezza delle API/configurazione dell'infrastruttura].
L'attività ha evidenziato una catena di vulnerabilità sfruttabili in sequenza che, partendo da un accesso anonimo da rete esterna, ha portato alla compromissione completa del backend e del database senza credenziali iniziali. I punti critici riguardano l'esposizione pubblica di un ambiente di sviluppo, la divulgazione di informazioni sensibili (backup utenti e specifica API), una SQL injection nel login che consente il bypass dell'autenticazione e una command injection che porta a RCE (esecuzione di codice remoto), seguita da movimento laterale via SSH e accesso al database MySQL interno.
Postura di sicurezza complessiva dell'applicazione: [Critical/High/Medium/Low]. Sono state identificate [x] vulnerabilità.

## Scope e Metodologia
URL Target: [url], endpoint API [/api/...], e infrastruttura backend raggiunta tramite le vulnerabilità in scope (host applicativo, container Docker, database MySQL).
Ruoli autenticati testati: [Non autenticato/Utente Standard/Admin].
Aree escluse: [Attacchi DoS/Stress Test/Social Engineering/Sistemi di Terze Parti].
Aree di test: [Injection/Broken Access Control/Cryptographic Failures/Security Misconfiguration/Authentication Failures].
Strumenti usati: [Burp Suite / fuff / Postman / Swagger Editor/mimikatz/hashcat/john the ripper / crackstation / cyberchef / nmap / sqlmap / ssh / bloodhound / metaploit / hydra / ghidra / wireshark / netcat / scapy / impacket].
Macchina attaccante: [x.x.x.x]

## Riepilogo dei findings

| ID  | Finding | Severity | CVSS 4.0 | Vettore CVSS |
| --- | ------- | -------- | -------- | ------------ |
|     |         |          |          |              |
|     |         |          |          |              |

## Findings Dettagliati

[[SQL Injection]]
Severity: [Critical/High/Medium/Low]
Injection URL: [url]
Metodo: [HTTP:POST]

Il form di [login/ricerca] non sanifica gli input prima di inserirli nella query SQL, consentendo il bypass dell'autenticazione tramite injection. È inoltre possibile autenticarsi mirando a un utente specifico, incluso l'amministratore.

Request:
Response:
Impatto:
Remediation:

--- 
[[Command Injection]]
Severity: [Critical/High/Medium/Low]
Injection URL: [url]
Metodo: [HTTP:POST]

L'endpoint passa il valore del parametro "q" a una shell di sistema senza sanitizzazione, consentendo l'iniezione di comandi arbitrari. È stata ottenuta una reverse shell verso la macchina attaccante.

Request:
Response:
Impatto:
Remediation:

--- 
[[IDOR & Broken Access Control|Broken Access Control]]
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:GET]

L'endpoint restituisce i dati degli utenti iterando sugli identificativi, senza controlli di autorizzazione. Tramite Postman è stato possibile enumerare gli account e identificare l'amministratore

Request:
Response:
Impatto:
Remediation:

---
Ambiente di sviluppo esposto pubblicamente
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:GET]

Il sottodominio .dev è raggiungibile pubblicamente da Internet ed espone funzionalità e dati non destinati alla produzione. È stato individuato tramite fuzzing di sottodomini con ffuf.

Request:
Response:
Impatto:
Remediation:

---
Information Disclosure
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:GET]

Il fuzzing di file e directory ha rivelato [x] percorsi sensibili:

Request:
Response:
Impatto:
Remediation:

---
Chiave privata SSH esposta
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:N/A]

Dalla shell ottenunta in [x], nella directory [x] erano presenti la chiave privata [x] e il file [x] (da cui si ricava lo username valido), consentendo l'accesso SSH come utente legittimo.

Request:
Response:
Impatto:
Remediation:

--- 
Segreti in chiaro nel file
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:N/A]

Il file .env del progetto conteneva credenziali e parametri di configurazione in chiaro, incluse le informazioni di accesso al database. La rete dei container è stata mappata con [x]

Request:
Response:
Impatto:
Remediation:

---
Accesso non autorizzato al database
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:N/A]

Con le credenziali e l'IP ricavati in [Vuln. x], è stato possibile connettersi al database MySQL interno e interrogare le tabelle. Nella tabella [x] è stato individuato un dump di credenziali; l'hash di un altro utente è risultato un MD5 non salato ed è stato sottoposto a cracking.

Request:
Response:
Impatto:
Remediation:

--- 
Esposizione informazione passiva
Severity: [Critical/High/Medium/Low]
URL Interessato: [url]
Metodo: [HTTP:N/A]

L'organizzazione espone pubblicamente informazioni che aggregate facilitano le fasi di ricognizione e gli attacchi mirati (spear phishing, password spraying, social engineering). La superficie informativa pubblica dovrebbe seguire il principio del minimo necessario.

Esempi riscontrati:
- Nominativi e ruoli tecnici nella pagina [x]. Pubblicare informazioni/dati riguardanti [x] fornisce ad un attaccante target precisi per phishing e per dedurre gli schemi degli username aziendali.
  È preferibile indicare ruoli e contatti funzionali (es. it@azienda.it) anziché persone identificabili.

## Raccomandazioni di Remediation
1. Utilizzare query parametrizzate o metodi ORM per tutte le interazioni con il database.
2. Implementare controlli di accesso lato server so ogni endpoint e risorsa
3. Eliminare l'esecuzione di comandi di sistema a partire da input utente.
4. Rimuovere ambienti di sviluppo, backup e documentazione API dall'esposizione pubblica.
5. Gestire chiavi e segreti tramite un vault dedicato; ruotare tutte le credenziali  compromesse.
6. Segregare a livello di rete il database dagli host applicativi.
7. Adottare algoritmi di hashing robusti e salati (bcrypt/argon2) e policy di password forti.

---

Vedi anche: [[Report HackTheBox]] · [[PROVA PRATICA ESAME]] · [[SQL Injection]] · [[Command Injection]] · [[IDOR & Broken Access Control]] · [[Authentication & Session Attacks]] · [[Recon & Enumeration]]

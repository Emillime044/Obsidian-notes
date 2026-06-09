## Hive

È un blocco di costruzione fondamentale che contiene un insieme di chiavi e valori del registro.
Il registro di sistema di Windows è un database gerarchico che memorizza configurazioni a basso livello per il sistema operativo.
Gli hive sono i file che contengono il database del registro di sistema e ognuno di essi rappresenta una raccolta di chiavi, sottoclassi e valori che rappresentano parti specifiche della configurazione del sistema.

## Hive principali

- HKEY_CLASSES_ROOT (HKCR): 
	- Contiene:
		- Registrazione dei componenti COM;
		- Associazioni dei tipi di file;
- HKEY_CURRENT_USER (HKCU):
	- Contiene:
		- Informazioni specifiche dell'utente attualmente connesso;
- HKEY_LOCAL_MACHINE (HKLM):
	- Contiene:
		- Impostazioni del sistema;
		- Configurazioni per l'hardware e il software installato;
- HKEY_USERS (HKU):
	- Contiene:
		- Informazioni specifiche per tutti gli utenti del sistema;
- HKEY_CURRENT_CONFIG (HKCC):
	- Contiene:
		- Collegamento alle informazioni di configurazione per l'hardware corrente del computer;

## Hive su file system

SYSTEM:
- Appartiene a HKEY_LOCAL_MACHINES\SYSTEM.
- Contiene:
	- Informazioni relative alla configurazione del sistema;
		- compresi driver di dispositivi, servizi e bootstrap di sistema;

SOFTWARE:
- Appartiene a HKEY_LOCAL_MACHINE\SOFTWARE.
- Contiene:
	- Informazioni su software e applicazioni installate nel sistema;
		- comprese impostazioni specifiche dalle applicazioni e le informazioni di configurazione a livello di sistema per il softare;

NTUSER.DAT:
- Hive specifico dell'utente, appartiene a HKEY_CURRENT_USER.
- Ogni utente ha un file NTUSER.DAT nella directory del profilo utente;
- Contiene:
	- Configurazioni e preferenze UI;

SECURITY:
- Appartiene a HKEY_LOCAL_MACHINE\SECURITY.
- Contiene:
	- Informazioni relative alla sicurezza del sistema;
	- Compresi criteri di sicurezza, account utente, gruppi, informazioni di sicurezza per vari oggetti del sistema;

SAM:
- Appartiene a HKEY_LOCAL_MACHINE\SAM.
- Contiene informazioni su:
	- Account utente e gruppi di sicurezza locali, insieme password;
	- Altre informazioni relative alla sicurezza degli account;

Amcache.hve:
- Usato da Windows per memorizzare informazioni dei programmi eseguiti e installati.
- Contiene dettagli come:
	- Nomi dei file;
	- Eseguibili;
	- Percorsi;
	- Hash SHA1;
	- Timestamp di esecuzione e metadati sull'installazione delle applicazioni;


## Restrizioni dei file di registro

Blocco esclusivo: Windows mantiene un blocco esclusivo per prevenire corruzione dei dati e garantire integrità delle informazioni.

Integrità del Sistema: Windows impedisce la copia o la modifica dei file mentre il sistema è in esecuzione.

Sicurezza: Windows limita l'accesso a quei file per proteggere le informazioni sensibili contenute da accessi non autorizzati o manipolazioni.
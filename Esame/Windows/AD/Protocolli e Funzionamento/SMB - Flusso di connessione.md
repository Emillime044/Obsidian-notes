---
tags:
  - protocollo
  - smb
  - active-directory
  - windows
---

# SMB — Flusso di connessione

> [!abstract] In breve
> SMB (Server Message Block) è il protocollo principale per il file sharing in ambienti Windows (porta **TCP 445**). Di seguito le fasi di una connessione client → share.

## Fasi della connessione

1. **Risoluzione del nome del server**
	- Tramite [[Risoluzione dei nomi in Windows|DNS]] (e relativi fallback).
2. **Stabilire una connessione di rete**
	- Il client avvia una connessione SMB (tramite NetBIOS o TCP/IP, **porta 445**).
3. **Autenticazione del client** — [[Kerberos - Ticket e autenticazione|Kerberos]] o NTLM
	- **Kerberos** (preferito in Active Directory):
		- Il client richiede un **TGT** (Ticket Granting Ticket) al **KDC** (Key Distribution Center).
		- Il client richiede poi un **Service Ticket** specifico per il server che ospita lo share.
	- **NTLM** (fallback):
		- Se Kerberos non è disponibile si usa NTLM, basato su un meccanismo **challenge-response**.
4. **Autorizzazione all'accesso** — ACL (Access Control Lists)
	- Una volta autenticato, il server verifica i permessi dell'utente sulla share tramite le **ACL** associate alla risorsa.
	- Possono includere permessi **espliciti** o **derivati da gruppi di AD**.
5. **Negoziazione delle capacità SMB** (SMBv1 / SMBv2 / SMBv3)
	- Client e server negoziano la versione di SMB e le funzionalità (es. crittografia, compressione).
6. **Connessione sicura (opzionale)**
	- **Crittografia SMB**: con SMBv3 il traffico può essere cifrato.
	- **SMB Signing**: garantisce l'integrità dei dati scambiati, prevenendo attacchi [[Attacchi Layer 2|MITM]] / [[Attacchi Active Directory#SMB Relay|SMB Relay]].
7. **Accesso ai dati**
	- Operazioni di lettura, scrittura e modifica su file e directory.
8. **Gestione delle sessioni** (per tutta la durata della connessione)
	- **Keep-Alive**: mantiene la connessione aperta.
	- **Timeout**.

![[Pasted image 20260608114656.png]]

## Dove SMB è critico in un dominio
- **SYSVOL**: condivisione SMB che ospita script di logon, GPO e file di configurazione del dominio.
- **Accesso a condivisioni di rete** sui server di dominio.
- **Replica AD DS**: alcune operazioni di replica interna usano SMB per sincronizzare i dati tra Domain Controller.

> [!warning] Superficie d'attacco
> SMB è bersaglio diretto di [[Attacchi Active Directory#SMB Relay|SMB Relay]] e indiretto del [[Attacchi Active Directory#LLMNR NBT-NS Poisoning|poisoning LLMNR/NBT-NS]]. Disabilitare SMBv1 e forzare il signing sono mitigazioni chiave.

---
tags:
  - concetto
  - windows
  - active-directory
  - autenticazione
---

# Token vs Ticket

> [!abstract] In breve
> Il **ticket** ([[Kerberos - Ticket e autenticazione|Kerberos]]) viaggia in rete e prova l'identità verso un servizio. Il **token** è una struttura **locale** dell'OS Windows che rappresenta privilegi e permessi dell'utente in una sessione.

## Access Token

Rappresentazione interna usata da Windows (incluso AD) per gestire **privilegi e permessi** di un utente.

- **Creato da:** Security Account Manager (SAM) o Local Security Authority Subsystem Service (**LSASS**).
- **Contiene:**
	1. SID utente
	2. Gruppi di appartenenza
	3. Diritti e privilegi
- **Validità:** solo per la sessione di autenticazione; legato all'ambiente **locale**, **non** trasmesso in rete.

Quando un utente si autentica su una macchina Windows, viene creato un token con i suoi diritti/privilegi, usato a ogni accesso a risorse locali o remote.

![[Pasted image 20260608122431.png]]

## Confronto rapido

| | **Token** | **Ticket** (Kerberos) |
|---|---|---|
| Ambito | Locale (OS) | Rete |
| Scopo | Autorizzazione: privilegi/permessi nella sessione | Autenticazione verso un servizio |
| Creato da | SAM / LSASS | KDC (AS + TGS) |
| Trasmesso in rete? | No | Sì |
| Contenuto | SID, gruppi, privilegi | Identità, session key, durata, flag |

> [!danger] Attacco correlato
> [[Attacchi Active Directory#Token Impersonation|Token Impersonation]] — abuso di token presenti in memoria per impersonare altri utenti (es. tecniche tipo `incognito`).

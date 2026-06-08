---
tags:
  - protocollo
  - kerberos
  - autenticazione
  - active-directory
---

# Kerberos — Ticket e autenticazione

> [!abstract] In breve
> Kerberos è il protocollo di autenticazione preferito in Active Directory. Si basa su due tipi di ticket emessi dal **KDC** (Key Distribution Center): il **TGT** e il **Service Ticket**.

## Tipi di ticket

### Ticket Granting Ticket (TGT)
- Rilasciato dal **KDC** al login dell'utente.
- Dimostra che il client è autenticato e può richiedere altri ticket **senza reinserire le credenziali**.
- Usabile **solo per richiedere altri ticket**, non per accedere direttamente ai servizi.

### Service Ticket
- Rilasciato dal **TGS** (Ticket Granting Service, componente del KDC) su richiesta del client, usando il TGT.
- **Specifico** per il servizio/server a cui il client vuole accedere.
- Garantisce l'accesso al servizio **senza rivelare credenziali sensibili**.

## Flusso di autenticazione

1. **AS Request** (richiesta iniziale al KDC)
	- Il client invia la richiesta all'**Authentication Server (AS)**.
	- Include: nome utente (principal name) e, opzionalmente, un timestamp.
2. **AS Response** (risposta del KDC)
	- Il KDC verifica le credenziali (es. password nel DB).
	- Se valide, invia il **TGT**, crittografato con la chiave segreta del KDC, contenente: identità utente, timestamp, durata.
	- Il TGT **non può essere letto dal client**.
3. **TGS Request** (richiesta di servizio)
	- Il client usa il TGT per richiedere accesso a un servizio specifico, inviando al **TGS**: TGT, nome servizio, autenticatore crittografato con la session key.
4. **TGS Response**
	- Il TGS verifica TGT e autenticatore.
	- Se validi, genera il **Service Ticket** (crittografato con la chiave del servizio) e una **nuova session key** client-servizio.
5. **Accesso al servizio**
	- Il client invia al servizio: Service Ticket + nuovo autenticatore crittografato con la session key del servizio.
	- Il server verifica ticket e autenticatore e concede l'accesso.

![[Pasted image 20260608120634.png]]

## Crittografia del Service Ticket

Il Service Ticket è crittografato dal KDC in **due parti**:

1. **Parte con la chiave del servizio (Service Key)** — nota solo a servizio e KDC. Assicura che solo il servizio richiesto possa decifrarlo. Contiene:
	- Identità client
	- Identità servizio
	- Session key condivisa (client-servizio)
	- Durata del ticket
	- Flag del ticket
2. **Parte con la session key (client-KDC)** — il KDC restituisce al client la nuova session key (client-servizio) cifrata con la session key esistente tra client e KDC, così solo il client può accedervi.

### Contenuto in dettaglio

| Campo | Dettaglio |
|---|---|
| **Identità client** | UPN (`username@realm`, es. `utente@DOMINIO.LOCAL`) o SID. |
| **Identità servizio** | SPN (`service/hostname`, es. `HTTP/server.dominio.local`). Il KDC lo usa per trovare la chiave del servizio. |
| **Session key (client-servizio)** | Chiave temporanea condivisa; inclusa due volte (cifrata con chiave del servizio e con session key del client). |
| **Durata** | Start Time + End Time. Default TGT in AD: **8 ore**. Rinnovabile se configurato. |
| **Flag** | Forwardable, Renewable, Initial, Pre-authenticated, Proxiable, Postdated. |

### Sicurezza
- **Algoritmi moderni:** AES (etype 17 o 18) per cifrare i ticket.
- **Durata limitata** (≈8h) riduce l'impatto di un ticket compromesso.
- **KDC** = componente centrale: gestisce tutte le chiavi segrete → va protetto rigorosamente.

> [!danger] Attacchi correlati
> - [[Attacchi Active Directory#Kerberoasting|Kerberoasting]] — abuso degli SPN per estrarre e crackare offline le chiavi dei service account.
> - [[Attacchi Active Directory#Golden Ticket|Golden Ticket]] — forgiatura di un TGT arbitrario con la chiave dell'account `krbtgt`.

> [!note] Nota terminologica
> "TGS" indica il **Ticket Granting Service** (componente del KDC). Il ticket che emette è il **Service Ticket** (a volte detto anch'esso "TGS ticket" / "ST"). Nei tuoi appunti originali "TGS" era usato a volte per indicare il ticket: qui lo tengo distinto per chiarezza.

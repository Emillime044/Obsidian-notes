- Risoluzione del nome del server:
	- DNS (Domain Name System)
- Stabilire una connessione di rete:
	- SMB (Server Message Block)
		- Client avvia una connessione SMB (tramite NetBIOS o TCP/IP, porta 445).
		- Protocollo principale file sharing in ambienti windows.
- Autenticazione del client:
	- Kerberos o NTLM
		- Kerberos (preferito in Active Directory)
			- Client richiede un ticket TGT (Ticket Granting Ticket) al KDC (Key Distribution Center).
			- Client richiede ticket di servizio (Service Ticket) specifico per il server che ospita lo share.
		- NTLM (fallback):
			- Se Kerberos non è disponibile viene usato il protocollo NTLM, che prevede un challenge-response per l'autenticazione.
- Autorizzazione all'accesso:
	- ACL (Access Control Lists)
		- Una volta autenticato, il server verifica se l'utente dispone dei permessi per accedere alla share. Determinato dalle ACL associate alla risorsa condivisa.
		- Possono includere sia permessi espliciti sia permessi derivati da gruppi di AD.
- Negoziazione delle capacità SMB:
	- SMB (SMBv1, SMBv2, SMBv3)
		- Client e server negoziano versione SMB da usare, specificando funzionalità come cittografia e compressione.
- Stabilire una connessione sicura (opzionale):
	- Meccanismi:
		- Crittografia SMB: Con SMBv3 il traffico può essere cifrato.
		- Signing SMB: Garantisce integrità dati scambiati, prevenendo attacchi MITM.
- Accesso ai dati:
	- Una volta autorizzato, client può accedere alla share. SMB consente operazioni tipo lettura, scrittura, modifica di file e directory.
- Gestione delle sessioni:
	- Durante l'intera connessione:
		- Keep-Alive: Usato per mantenere la connessione aperta.
		- TimeOut.

![[Pasted image 20260608114656.png]]


### Quando il DNS non risolve, entrano in gioco altri protocolli:

1. NetBIOS over TCP/IP (NetBT):
	1. Protocolli: NetBIOS Name Service (NBNS), NetBIOS Datagram Service, NetBIOS Session Service
	2. Cosa fa:
		1. Vecchio protocollo reti Windows per risolvere i nomi in indirizzi IP.
		   Se il DNS non riesce, client può inviare richiesta broadcast sulla rete locale p er cercare il nome del server (NetBIOS Name Query).
		   Il server corrispondere risponde con il proprio IP.
	3. Limitazioni:
		1. Funziona solo in reti locali o VPN.
		   Meno efficiente e sicuro rispetto al DNS.
2. LLMNR (Link-Local Multicast Name Resolution):
	1. Protocolli: UDP porta 5355
	2. Cosa fa:
		1. Protocollo Microsoft che consente ai dispositivi di risolvere nomi su reti locali (link-local) senza dipendere dal DNS.
		   Funziona inviando richieste multicast a tutti i dispositivi sulla rete locale.
	3. Limitazioni:
		1. Limitato alla rete locale.
		   Meno sicuro e debole contro attacchi come spoofing.
3. mDNS (Multicast DNS):
	1. Protocolli: UDP porta 5353
	2. Cosa fa:
		1. mDNS è un protocollo simile a LLMNR, utilizzato principalmente in ambienti non Windows.
		   Risolve i nomi dei dispositivi sulla rete locale tramite richieste multicast, senza un server DNS centralizzato.
	3. Limitazioni:
		1. Orientato a reti locali.
		   Meno comune nei domini Active Directory standard.
4. File HOSTS:
	1. Meccanismo: Static Hostname resolution
	2. Cosa fa:
		1. OS controlla il file hosts per trovare una mappatura statica tra nomi e IP.
	3. Limitazioni:
		1. Deve essere configurato manualmente.
		   Non è scalabile in reti più grandi.
5. WINS (Windows Internet Name Service):
	1. Protocollo: NetBIOS over TCP/IP
	2. Cosa fa:
		1. Servizio centralizzato per risolvere i nomi NetBIOS in IP
		   Sorta di DNS per i nomi NetBIOS, deprecato e sostituito dal DNS.
	3. Limitazioni:
		1. Obsoleto e raramente usato nelle reti moderne.

## Ordine di risoluzione tipico in Windows

1. Controllo del file hosts.
2. Query al server DNS.
3. Query tramite NetBIOS (broadcast o WINS, se configurato).
4. Query tramite LLMNR o mDNS (se supportati e abilitati).

![[Pasted image 20260608115640.png]]



## Tickets:

Ticket Granting Ticket (TGT):
	Rilasciato dal KDC (Key Distribution Center) al momento del login dell'utente.
	Dimostra che il client è autenticato e autorizzato a richiedere ulteriori ticket senza reinserire credenziali.
	Usabile solo per richiedere altri ticket, non per accedere ai servizi.

Service Ticket:
	Rilasciato dal Ticket Granting Service (TGS), una componente del KDC, su richiesta del client, usando il TGT.
	Specifico per il servizio o il server a cui il client vuole accedere.
	Garantisce che il client abbia il permesso di accedere a quel servizio senza rivelare credenziali sensibili.


## Flusso di autenticazione

1. Richiesta iniziale al KDC (AS Request):
	1. Client invia richiesta di autenticazione al Authentication Server (AS).
	2. Include:
		1. Nome utente (principal name).
		2. Timestamp (opzionale).
2. Risposta del KDC (AS Response):
	1. KDC verifica le credenziali dell'utente (es. tramite password memorizzata nel DB)
	2. Se valido il KDC invia:
		1. TGT (Ticket Granting Ticket): Ticket crittografato con chiave segreta del KDC.
		2. Contiene:
			1. Identità dell'utente.
			2. Timestamp.
			3. Durata del ticket.
	3. TGT Crittografato e non può essere letto dal client.
3. Richiesta di servizio (TGS Request):
	1. Client usa il TGT per richiedere accesso a un servizio specfico.
	2. Invio al Ticket Granting Service (TGS):
		1. TGT.
		2. Nome servizio richiesto.
		3. Autenticatore crittografato con session key.
4. Risposta del TGS (TGS Response):
	1. TGS verifica il TGT e l'autenticatore.
	2. Se valido genera:
		1. Service Ticket: ticket crittografato con chiave segreta del server del servizio.
		2. Nuova session key per comunicare con il servizio.
5. Accesso al servizio:
	1. Client invia al servizio:
		1. Service Ticket.
		2. Nuovo autenticatore crittografato con session key del servizio.
	2. Server verifica ticket e autenticatore.
	3. Se valido, server concede accesso al servizio.

![[Pasted image 20260608120634.png]]


## Ticket Encryption

TGS crittografato dal KDC in 2 modi:
1. Parte crittografata con la chiave del servizio:
	1. Corpo principale TGS crittografato usando chiave segreta del servizio (Service Key), nota solo a servizio e KDC.
	2. Assicura che solo il servizio richiesto può decifrare e leggere il TGS.
	3. Contenuto crittografato:
		1. Identità client.
		2. Identità servizio.
		3. Chiave di sessione condivisa (client-servizio).
		4. Durata del ticket.
		5. Flag del ticket.
2. Parte crittografata con la chiave di sessione (client-KDC):
	1. KDC restituisce il TGS al client insieme a nuova chiave di sessione condivisa (tra client e servizio)
	2. Crittografata con chiave di sessione esistente tra client e KDC.
	3. Assicura che solo il client può accedere alla chiave di sessione.

### Contenuto crittografato

1. Identità del client:
	1. Generalmente è uno tra i due:
		1. Principal Name (UPN, User Principal Name) 
		2. Security Identifier (SID)
	2. Scritto come:
		```username@realm```
		es. ```utente@DOMINIO.LOCAL```
		dove realm è il dominio Kerberos
	3. Servizio che riceve il TGS può verificare identità del client e concedere o negare l'accesso.
2. Identità del servizio:
	1. Server Principal name (SPN)
	2. Formato SPN:
		```service/hostname```
		es. ```HTTP/server.dominio.local```
	3. KDC usa l'SPN per individuare chiave segreta del servizio, necessaria per crittografare il TGS.
	4. Servizio usa questa info per verificare che il ticket sia destinato a lui.
3. Chiave di sessione condivisa (client-servizio):
	1. Chiave temporanea condivisa tra client e servizio. Usata per proteggere comunicazione tra client e servizio.
	2. Chiave di sessione inclusa nel TGS in due modi:
		1. Crittografata con chiave segreta del servizio
		2. Crittografata con chiave sessione del client
	3. Garantisce che client e servizio possano comunicare in modo sicuro, evitando uso di chiavi permanenti o statiche.
4. Durata del ticket:
	1. Periodo di validità del TGS, fornito dal KDC.
	2. Include 2 timestamp:
		1. Start Time
		2. End Time
		3. Durata predefinita TGS in AD 8 ore.
	3. Aiuta a mitigare i rischi associati a ticket rubati o compromessi.
	4. Se configurato come rinnovabile, client può richiedere rinnovo prima della scadenza.
5. Flag del ticket:
	1. Serie di bit che descrivono proprietà o comportamenti del ticket.
	2. Esempi di flag comuni:
		1. Forwardable: inoltrabile ad altri servizi.
		2. Renewable.
		3. Initial: ticket stato emesso come parte del processo iniziale di autenticazione.
		4. Pre-authenticated: client ha superato la pre-autenticazione.
		5. Proxiable: permette emissione ticket proxy per accedere a un altro servizio per conto del client.
		6. Postdated: ticket valido a partire da un'ora futura.

### Sicurezza ticket encryption

Algoritmi moderni:
- AES (etype 17 o 18) usato per cifrare TGS
Durata dei ticket:
- TGS durata limitata (di solito 8 ore), riducendo impatto di un ticket compromesso.
KDC:
- KDC componente centrale di kerberos, deve essere protetto rigorosamente perché gestisce tutte le chiavi segrete.
Replica dei file di sistema (SYSVOL):
- Condivisione SMB dove vengono archiviati script di accesso, GPO e altri file necessari a configurazione dominio.
Accesso a condivisioni di rete:
- Utenti e sistemi spesso accedono a codivisioni di rete su server di dominio.
Replica dei database del dominio (AD DS):
- Alcune operazioni replica interna AD si basano su SMB per sincronizzare dati tra i controller di dominio. 

## Differenza TOKEN e TICKET

Token è una rappresentazione interna usata per gestire privilegi e permessi di un utente nel contesto dell'OS Windows, incluso AD.

Creato da uno tra i due: 
- Security Account Manager (SAM) 
- Local Security Authority Subsystem Service (LSASS)

Contiene:
1. SID utente
2. Gruppi di appartenenza
3. Diritti e privilegi

Rimane valido solo per sessione di autenticazione. Legato all'ambiente locale e non viene trasmesso in rete.
Quando un utente si autentica a una macchina Windows, viene creato un token che include i dettagli relativi ai suoi diritti e privilegi. Questo token è utilizzato ogni volta che l'utente tenta di accedere a risorse locali o remote.

![[Pasted image 20260608122431.png]]


## Monitoring

- LLMNR/NBT-NS Poisoning:
	- Eventi generati:
		- 4624: accesso riuscito
		- 4625: accesso fallito
		- 4776: tentativo di autenticazione NTLM
- SMB Relay:
	- Eventi generati:
		- 4624 con logon type 3 (autenticazione da IP o host non autorizzato).
		- 4625
- Kerberoasting:
	- Eventi generati:
		- 4769: richiesta TGS
		- 4741: creazione di nuovo account di computer
- Mimikatz:
	- Eventi generati:
		- 4688: creazione di processo
		- 4673: utilizzo di privilegi sensibili
		- 4624 con logon type 9
- Token impersonation:
	- Eventi generati:
		- 4648
		- 4672: privilegi speciali assegnati
- Golden Ticket:
	- 4624 con logon type 3 o 9
	- 4769: richiesta TGS
---
tags:
  - protocollo
  - windows
  - active-directory
  - risoluzione-nomi
---

# Risoluzione dei nomi in Windows

> [!abstract] In breve
> Quando il **DNS non risolve** un nome, Windows ricorre a una serie di protocolli di fallback. Alcuni di questi (LLMNR, NBT-NS) sono insicuri e vengono sfruttati dal [[Attacchi Active Directory#LLMNR NBT-NS Poisoning|poisoning LLMNR/NBT-NS]].

## Protocolli di fallback

### 1. NetBIOS over TCP/IP (NetBT)
- **Protocolli:** NetBIOS Name Service (NBNS), Datagram Service, Session Service.
- **Cosa fa:** vecchio protocollo per risolvere nomi in IP. Se il DNS fallisce, il client invia una richiesta **broadcast** sulla LAN (NetBIOS Name Query); il server corrispondente risponde con il proprio IP.
- **Limitazioni:** funziona solo su reti locali o VPN; meno efficiente e sicuro del DNS.

### 2. LLMNR (Link-Local Multicast Name Resolution)
- **Protocollo:** UDP **porta 5355**.
- **Cosa fa:** protocollo Microsoft per risolvere nomi su reti link-local senza DNS, tramite richieste **multicast** a tutti i dispositivi della LAN.
- **Limitazioni:** limitato alla rete locale; debole contro lo **spoofing**.

### 3. mDNS (Multicast DNS)
- **Protocollo:** UDP **porta 5353**.
- **Cosa fa:** simile a LLMNR, usato soprattutto in ambienti non-Windows. Risolve i nomi dei dispositivi sulla LAN via multicast, senza DNS centralizzato.
- **Limitazioni:** orientato a reti locali; poco comune nei domini AD standard.

### 4. File HOSTS
- **Meccanismo:** static hostname resolution.
- **Cosa fa:** l'OS controlla il file `hosts` per una mappatura statica nome → IP.
- **Limitazioni:** configurazione manuale; non scalabile.

### 5. WINS (Windows Internet Name Service)
- **Protocollo:** NetBIOS over TCP/IP.
- **Cosa fa:** servizio centralizzato per risolvere nomi NetBIOS in IP (una sorta di "DNS per NetBIOS").
- **Limitazioni:** obsoleto, sostituito dal DNS, raro nelle reti moderne.

## Ordine di risoluzione tipico in Windows

1. Controllo del file `hosts`.
2. Query al server **DNS**.
3. Query tramite **NetBIOS** (broadcast o WINS, se configurato).
4. Query tramite **LLMNR** o **mDNS** (se supportati e abilitati).

![[Pasted image 20260608115640.png]]

> [!danger] Implicazione di sicurezza
> I passaggi 3 e 4 sono **broadcast/multicast non autenticati**: un attaccante sulla stessa LAN può rispondere prima del server legittimo e dirottare l'autenticazione → vedi [[Attacchi Active Directory#LLMNR NBT-NS Poisoning|LLMNR/NBT-NS Poisoning]]. Mitigazione principale: **disabilitare LLMNR e NBT-NS** via GPO.

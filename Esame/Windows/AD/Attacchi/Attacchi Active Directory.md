---
tags:
  - attacco
  - active-directory
  - kerberos
  - ntlm
---

# Attacchi Active Directory

## LLMNR / NBT-NS Poisoning
- **Tecnica:** l'attaccante risponde alle query broadcast/multicast dei protocolli di [[Risoluzione dei nomi in Windows#Protocolli di fallback|fallback]] (LLMNR, NBT-NS) spacciandosi per l'host cercato, catturando l'hash NTLMv2 della vittima.
- **Obiettivo:** raccolta credenziali (hash da crackare offline) o relay.
- **Mitigazione:** disabilitare LLMNR e NBT-NS via GPO.

## SMB Relay
- **Tecnica:** l'hash/handshake catturato (spesso via poisoning) viene **inoltrato in tempo reale** a un altro host che accetta autenticazione NTLM, autenticandosi come la vittima senza crackare nulla.
- **Obiettivo:** accesso non autorizzato a sistemi/share.
- **Mitigazione:** **SMB Signing** obbligatorio, disabilitare NTLM dove possibile.

## Kerberoasting
- **Tecnica:** un utente autenticato richiede [[Kerberos - Ticket e autenticazione|Service Ticket]] per account di servizio (con SPN); il ticket è cifrato con l'hash della password del service account → si **cracca offline**.
- **Obiettivo:** ottenere le credenziali dei service account (spesso privilegiati).
- **Mitigazione:** password lunghe/complesse per i service account, gMSA, AES invece di RC4.

## Token Impersonation
- **Tecnica:** abuso di [[Token vs Ticket|access token]] presenti in memoria su un host compromesso per impersonare altri utenti loggati.
- **Obiettivo:** escalation / movimento laterale con l'identità di un altro utente.
- **Mitigazione:** principio del least privilege, limitare login interattivi di account privilegiati.

## Mimikatz (credential dumping)
- **Tecnica:** estrazione da memoria (LSASS) di hash, ticket Kerberos e credenziali in chiaro; abilita pass-the-hash / pass-the-ticket.
- **Obiettivo:** furto credenziali e movimento laterale.
- **Mitigazione:** Credential Guard, protezione LSASS (RunAsPPL), EDR.

## Golden Ticket
- **Tecnica:** con la chiave dell'account **`krbtgt`** l'attaccante **forgia un TGT arbitrario**, ottenendo accesso illimitato e persistente al dominio.
- **Obiettivo:** persistenza e controllo totale dominio (qualsiasi identità/privilegio).
- **Mitigazione:** **doppio reset** della password `krbtgt`, protezione rigorosa del KDC/DC.

---

Vedi anche: [[Attacchi Layer 2]] · [[Detection - Event ID Windows]]

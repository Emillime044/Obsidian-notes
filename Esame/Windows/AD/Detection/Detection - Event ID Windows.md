---
tags:
  - detection
  - blue-team
  - event-id
  - active-directory
---

# Detection — Event ID Windows

> [!abstract] In breve
> Mappatura tra attacchi ([[Attacchi Active Directory]]) e gli **Event ID** Windows utili a rilevarli.

## Tabella attacco → Event ID

| Attacco | Event ID | Significato |
|---|---|---|
| [[Attacchi Active Directory#LLMNR NBT-NS Poisoning\|LLMNR / NBT-NS Poisoning]] | **4624** / **4625** / **4776** | Logon riuscito / fallito / tentativo auth NTLM |
| [[Attacchi Active Directory#SMB Relay\|SMB Relay]] | **4624** (logon type **3**) / **4625** | Logon di rete da IP/host non autorizzato |
| [[Attacchi Active Directory#Kerberoasting\|Kerberoasting]] | **4769** / **4741** | Richiesta TGS / creazione account computer |
| [[Attacchi Active Directory#Mimikatz credential dumping\|Mimikatz]] | **4688** / **4673** / **4624** (type **9**) | Creazione processo / uso privilegi sensibili / NewCredentials |
| [[Attacchi Active Directory#Token Impersonation\|Token Impersonation]] | **4648** / **4672** | Logon con credenziali esplicite / privilegi speciali assegnati |
| [[Attacchi Active Directory#Golden Ticket\|Golden Ticket]] | **4624** (type **3**/**9**) / **4769** | Logon di rete o NewCredentials / richiesta TGS |

## Glossario Event ID

| ID | Descrizione |
|---|---|
| **4624** | Account loggato con successo |
| **4625** | Tentativo di logon fallito |
| **4648** | Logon con credenziali esplicite (runas) |
| **4672** | Privilegi speciali assegnati a un nuovo logon |
| **4673** | Utilizzo di un privilegio sensibile |
| **4688** | Creazione di un nuovo processo |
| **4741** | Creazione di un nuovo account computer |
| **4769** | Richiesta di un Service Ticket Kerberos (TGS) |
| **4776** | Tentativo di validazione credenziali NTLM (sul DC) |

## Logon Type utili

| Type | Significato |
|---|---|
| **3** | Network (es. accesso a share SMB) |
| **9** | NewCredentials (`runas /netonly`, tipico di pass-the-hash) |

---

Vedi anche: [[Attacchi Active Directory]] · [[Attacchi Layer 2]]

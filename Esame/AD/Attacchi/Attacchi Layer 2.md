---
tags:
  - attacco
  - layer2
  - networking
  - mitm
---

# Attacchi Layer 2

> [!abstract] In breve
> Attacchi che sfruttano debolezze a livello data-link (switch, ARP, DHCP, VLAN, STP). Spesso il preludio a un **MITM** o a uno sniffing di rete.

## Tabella riepilogo

| Attacco | Obiettivo | Mitigazione chiave |
|---|---|---|
| ARP Spoofing | MITM / DoS | Dynamic ARP Inspection, static ARP |
| DHCP Spoofing | Controllo traffico / intercettazione | DHCP Snooping |
| DHCP Starvation | DoS sul DHCP | Rate limiting, DHCP Snooping |
| MAC Flooding | Sniffing (switch in "fail-open") | Port Security |
| STP Attack | MITM / DoS | BPDU Guard, Root Guard |
| VLAN Hopping | Intercettare traffico inter-VLAN | Disabilitare trunk inutili, VACL |
| MITM L2 | Intercettare/modificare traffico | 802.1X, TLS/IPSec |

---

## ARP Spoofing
- **Tecnica:** invio di pacchetti ARP falsificati per associare il proprio MAC a un IP legittimo, intercettando o manipolando il traffico.
- **Obiettivo:** intercettazione del traffico (**MITM**), dirottamento, DoS.
- **Mitigazione:** Dynamic ARP Inspection (DAI), static ARP entries.

## DHCP Spoofing
- **Tecnica:** creazione di un **server DHCP falso** che distribuisce configurazioni IP malevole ai dispositivi (es. gateway/DNS controllato dall'attaccante).
- **Obiettivo:** controllo del traffico di rete, intercettazione dei dati.
- **Mitigazione:** DHCP Snooping, autenticazione delle porte switch.

## DHCP Starvation
- **Tecnica:** invio di numerose richieste DHCP per **esaurire il pool** del server DHCP legittimo.
- **Obiettivo:** DoS contro il server DHCP (spesso abbinato a DHCP Spoofing per sostituirlo).
- **Mitigazione:** rate limiting sulle richieste DHCP, DHCP Snooping.

## MAC Flooding
- **Tecnica:** invio di una grande quantità di MAC falsi allo switch per **saturarne la tabella CAM**.
- **Obiettivo:** forzare lo switch a inoltrare il traffico su tutte le porte (comportamento "fail-open"/hub), favorendo lo **sniffing**.
- **Mitigazione:** Port Security, limitazione del numero di MAC per porta.

## STP Attack
> [!warning] Correzione rispetto agli appunti originali
> Negli appunti questa voce riportava (per errore di copia-incolla) la stessa descrizione del **MAC Flooding**. Qui c'è il contenuto corretto.

- **Tecnica:** l'attaccante invia **BPDU** (Bridge Protocol Data Unit) falsificate annunciando una **bridge priority più bassa (superiore)** per diventare il **root bridge** della topologia Spanning Tree. Il traffico viene così reinstradato attraverso la sua macchina.
- **Obiettivo:** **MITM** (traffico ridiretto attraverso l'attaccante) oppure **DoS/instabilità** (ricalcoli continui della topologia).
- **Mitigazione:** **BPDU Guard**, **Root Guard**, PortFast solo sulle porte di accesso, disabilitare STP dove non serve.

## VLAN Hopping
- **Tecnica:** forzare il traffico a uscire dalla VLAN assegnata.
	- *Metodo 1 — Double Tagging:* aggiunta di due tag VLAN (sfrutta la native VLAN del trunk).
	- *Metodo 2 — Switch Spoofing:* l'host simula uno switch e negozia un trunk (DTP).
- **Obiettivo:** intercettare traffico tra VLAN diverse.
- **Mitigazione:** disabilitare il trunking non necessario (`switchport mode access`, niente DTP auto), usare VLAN Access Control List (VACL), cambiare la native VLAN.

## Man-In-The-Middle (MITM) a livello L2
- **Tecnica:** uso di ARP Spoofing o DHCP Spoofing per posizionarsi tra due dispositivi in comunicazione.
- **Obiettivo:** intercettare, modificare o bloccare il traffico.
- **Mitigazione:** autenticazione **802.1X**, crittografia (**TLS/IPSec**).

---

Vedi anche: [[Attacchi Active Directory]] · [[Detection - Event ID Windows]]

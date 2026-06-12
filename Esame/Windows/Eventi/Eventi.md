
| Event ID | Sorgente | Descrizione                            | Criticità                            |
| -------- | -------- | -------------------------------------- | ------------------------------------ |


## Eventi Windows

| Event ID | Sorgente | Descrizione                     | Criticità                            |
| -------- | -------- | ------------------------------- | ------------------------------------ |
| 4624     | Security | Logon riuscito                  | Analizzare tipo di logon (2,3,10,11) |
| 4625     | Security | Logon fallito                   | Brute foce, password spray           |
| 4672     | Security | Assegnazione privilegi speciali | Escalation                           |
| 4720     | Security | Creazione nuovo account         | Account sospetto                     |
| 4726     | Security | Eliminazione account            | Cancellazione tracce                 |

## Eventi SYSMON


| Event ID | Sorgente           | Descrizione                                | Criticità                    |
| -------- | ------------------ | ------------------------------------------ | ---------------------------- |
| 1        | Process Creation   | Nome, path, command line, hash, parent PID | Execution & lateral movement |
| 3        | Network connection | Connessioni TCP/UDP, IP remoti             | C2 beaconing, tunneling      |

---

Vedi anche: [[Detection - Event ID Windows]] · [[Windows Hives]] · [[MACB]] · [[MFT]] · [[Splunk]]

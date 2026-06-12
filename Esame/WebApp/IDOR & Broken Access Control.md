## IDOR (Insecure Direct Object Reference)

L'app usa un identificatore (id, filename) preso dall'utente per accedere a un oggetto senza verificare che quell'utente abbia il diritto.

### Sfruttamento
```
	GET /account?id=1001
	GET /account?id=1002
	GET /invoice/1002.pdf
	POST /api/user/1002/role
```
- Si trova cambiando id numerici (incrementi/decrementi), UUID prevedibili, nomi file.
  Burp Intruder per ciclare gli id.

### Mitigazione

Autorizzazione lato server su ogni oggetto (controlla owner/ruolo), riferimenti indiretti/non prevedibili, deny-by-default

---

Vedi anche: [[Authentication & Session Attacks]] · [[Report template]] · [[Recon & Enumeration]]
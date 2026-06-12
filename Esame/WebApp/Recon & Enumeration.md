## Scan di porte e servizi

```
	nmap -sV -sC -p x TARGET
	
	-sV: scan delle porte per determinare servizio/versione
	-sC: equivalente di --script=default
	-p: port
```

```
	ffuf -u https://TARGET/FUZZ -w /usr/share/wordlists/wordlist.txt

	-u: url
	-w: wordlist
	-mc: match status code
```

---

Vedi anche: [[SQL Injection]] · [[Command Injection]] · [[Path Traversal & LFI, RFI]] · [[Insecure File Upload]] · [[IDOR & Broken Access Control]] · [[Authentication & Session Attacks]] · [[Cross-Site Scripting (XSS)]] · [[CSRF]] · [[Report template]]



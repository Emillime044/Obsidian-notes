- Brute force / password spraying (login):
```
	hydra -l admin -P /usr/share/wordlists/rockyoiu.txt TARGET http-post-form "/login:username^USER^&password=^PASS^:F=Invalid"
	-l: user singolo
	-P wordlist password
	http-post-form "path:body:fail_string":^USER^/^PASS^ sono placeholder
	F= stringa che indica login faillito
```
- Credenziali di default: sempre da provare;
- Session fixation / cookie deboli: cookie prevedibili o non rigenerati al login;
- JWT: controlla alg:none, secret deboli (hashcat), claim ```role``` manipolabili;
- Password reset logic flaws: token prevedibili, host header injection nel link di reset;

### Mitigazione

Rate limiting + lockout, hashing forte (bcrypt/argon2), MFA, rigenerazione sessione al login, cookie sicuri (vedi [[Cross-Site Scripting (XSS)|XSS]]), token reset random e a scadenza.

---

Vedi anche: [[SQL Injection]] · [[Cross-Site Scripting (XSS)]] · [[CSRF]] · [[Recon & Enumeration]]
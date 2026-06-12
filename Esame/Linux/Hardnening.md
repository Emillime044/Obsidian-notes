## Rimuovere tutti i servizi non necessari

Visualizza tutti i servizi installati e il loro stato
```
	systemctl list-unit-file --type=service
```

I servizi non usati vanno rimossi o almeno fermati e disabilitati
```
	systemctl stop <nomeServizio>
	systemctl disable <nomeServizio>
```

Impedire avvio o abilitazione di un servizio per errore:
```
	systemctl mask <nomeServizio>
```
*Usare unmask per consentire avvio o abilitazione del servizio*

Verificare i servizi in ascolto su porte tcp/udp
```
	netstat -tulpn
```

## Compilare il kernel solo con feature che servono

Installare sorgenti del kernel e tool di compilazione
```
	sudo apt-get install linux-source
	sudo apt-get install build-essential libncurses-dev bison flex libssl-dev libelf-dev
```

Aprire menu di configurazione parametri kernel:
```
	cd /path/to/linux-source-directory
	sudo make menuconfig
```

Compilare e installare kernel nuovo:
```
	sudo make
	sudo make install
	sudo update-grub2
```

## Protezione attacchi DoS / DDoS

Abilitare SYNCOOKIES
- Il server risponde a richieste SYN valide con un token crittografato;
- Token inviato con SYN-ACK al client;
- Cookie inserito nel campo "Initial Sequence Number" del SYN-ACK;
- Se il client nell'ACK risponde con il token corretto viene stabilita la connessione;
```
	echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf
	sysctl -p
```

## Protezione attacchi di tipo smurf

Settando la flag "net.ipv4.icmp_echo_ignore_broadcasts" a 1, il sistema ignora richieste di eco ICMP inviate al broadcast.

```
	echo "net.ipv4.icmp_echo_ignore_broadcasts = 1" >> /etc/sysctl.conf
	sysctl -p
```

## Protezione attacchi IP spoofing

Verifica percorso inverso di tutti i pacchetti IP in arrivo su tutte le interfacce di rete.
Default:
- Kernel applica verifica percorso inverso solo a pacchetti IP in arrivo su tutte le interfacce tranne quelle che il kernel considera come "interfacce deboli";
Interfacce deboli:
- Interfacce che hanno indirizzi IP non routabili o non attendibili;
	- Es. Looback o interfacce virtuali

```
Abilita RPF (reverse path forwarding) per impedire il routing asimmetrico:	
	echo "net.ipv4.conf.all.rp_filter = 1" >> /etc/sysctl.conf
	echo "net.ipv4.conf.default.rp_filter = 1" >> /etc/sysctl.conf
Oppure solo su un'interfaccia:
	echo "net.ipv4.conf.eth0.rp_filter = 1" >> /etc/sysctl.conf
	sysctl -p
```

## auditd

Demone principale del Linux Auditing System.
Monitora e registra eventi di sicurezza a livello kernel.
Una volta installato raccogli informazioni su accessi a file, comandi eseguiti, modifiche ai permessi e operazioni amministrative.

---

Vedi anche: [[Splunk]]
### RSA (Ridest Shamir Adleman):
Algoritmo più usato che sta venendo pian piano sostituito dalla **ECC** (Elliptic Curve Cryptography).

RSA basato sulla mancanza di un metodo matematico per fattorizzare grandi numeri.
- Generazione chiavi basata sulla scelta di due numeri primi molto grandi.

Vengono generati 2 numeri primi molto grandi P e Q che devono rimanere segreti e si calcola N:
```
	N = Kp1 = P*Q
	
	Kp1 = prima parte della chiave pubblica
```

Di seguito si calcola:
```
	B = (P-1)(Q-1)
```

E si determina un numero E che corrisponda ai seguiti requisiti:
- Non abbia divisori in comune che B;
- Risulti 1 < E < B;

E è la seconda parte della chiave pubblica (Kp2).

```
	Kpub = (Kp1;Kp2) = (N;E)
```


### Generazione della chiave privata

Viene generato D, un numero minore di B (```B=(P-1)(Q-1)```) tale che:
```
	(D*E)modB = 1
```


### Cifrare P e decifrare C

Mittente: Bob;
Destinatario: Alice;

Bob esegue ```C=P^E MOD N```

Per decifrare C, Alice esegue ```P=C^D MOD N```


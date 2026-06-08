### Il problema

Nella tua scena ci sono molti oggetti. Un [[Raggio (Ray)|raggio]] può intersecare più di una [[L'equazione della sfera|sfera]]. Quale intersezione ([[Hit detection Raggio-Sfera]]) "conta"? Quella **più vicina** alla camera, ovviamente: gli oggetti davanti nascondono quelli dietro.

### Cosa succede senza tracking

Senza tenere traccia della distanza, potresti colorare il pixel in base all'**ultima** intersezione trovata, non la più vicina. Risultato: gli oggetti lontani appaiono davanti a quelli vicini, un caos totale.

### Come funziona con t_min e t_max

Quando cerchi intersezioni, mantieni un intervallo di t validi: [t_min, t_max].

- **t_min** (di solito un piccolo valore come 0.001, non zero) indica la distanza minima accettabile. Perché non zero? Per evitare il "shadow acne": a causa di errori di arrotondamento, il [[Raggio (Ray)|raggio]] potrebbe ri-intersecare la stessa superficie da cui è appena partito, a t praticamente zero. Un piccolo t_min evita questo.
- **t_max** inizia a +infinito (o un numero molto grande).

Il procedimento è:

1. Per ogni oggetto nella scena, controlla se il [[Raggio (Ray)|raggio]] lo interseca.
2. Se sì, e se il t dell'intersezione è nell'intervallo (t_min, t_max), registra questo hit e **aggiorna t_max** al t appena trovato.
3. Al prossimo oggetto, l'intervallo è più stretto: accetti solo intersezioni **ancora più vicine** della migliore trovata finora.
4. Alla fine del ciclo, hai l'intersezione più vicina.
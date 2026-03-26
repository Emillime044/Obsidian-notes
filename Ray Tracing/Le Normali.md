Una normale è un <a href="obsidian://open?vault=Bobobob&file=Ray%20Tracing%2FVettori%203D">vettore</a> che punta perpendicolarmente alla superficie in un dato punto.

### Come calcolarlo su una sfera

Su una sfera è facilissimo: in un punto P sulla supericie, la normale punta dal centro C verso P.

```
N = P - c
```

### Perché si normalizza

Il <a href="obsidian://open?vault=Bobobob&file=Ray%20Tracing%2FVettori%203D">vettore</a> P - C ha lunghezza r (il [[Raggio (Ray)]] della sfera). Per comodità nei calcoli successivi, lo si normalizza.

```
N = (P - C) / |P - C| = (P - C) / r
```

Un <a href="obsidian://open?vault=Bobobob&file=Ray%20Tracing%2FVettori%203D">vettore</a> normale unitario (di lunghezza 1) semplifica enormemente i calcoli di illuminazione. Per esempio, se fai il dot product tra la normale e la direzione della luce, ottieni direttamente il coseno dell'angolo - senza fattori di scala.

### A cosa servono le normali nel ray tracing

Le normali sono fondamentali per:
- **Decidere il colore**: la tecnica base è colorare un pixel in base alla direzione della normale (vedi sfondo xd).
- **Calcolare l'illuminazione**: quanto è illuminato un punto dipende dall'angolo tra la normale e la direzione della luce.
- **Far rimbalzare i raggi**: quando un [[Raggio (Ray)]] colpisce una superficie, la direzione del rimbalzo dipende dalla normale.

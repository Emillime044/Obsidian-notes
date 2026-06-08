Una normale è un [[Vettori 3D|vettore]] che punta perpendicolarmente alla superficie in un dato punto.

### Come calcolarlo su una sfera

Su una [[L'equazione della sfera|sfera]] è facilissimo: in un punto P sulla superficie, la normale punta dal centro C verso P.

```
N = P - C
```

### Perché si normalizza

Il [[Vettori 3D|vettore]] P - C ha lunghezza r (il raggio della sfera). Per comodità nei calcoli successivi, lo si normalizza.

```
N = (P - C) / |P - C| = (P - C) / r
```

Un [[Vettori 3D|vettore]] normale unitario (di lunghezza 1) semplifica enormemente i calcoli di illuminazione. Per esempio, se fai il dot product tra la normale e la direzione della luce, ottieni direttamente il coseno dell'angolo - senza fattori di scala.

### A cosa servono le normali nel ray tracing

Le normali sono fondamentali per:

- **Decidere il colore**: la tecnica base è colorare un pixel in base alla direzione della normale (vedi sfondo xd).
- **Calcolare l'illuminazione**: quanto è illuminato un punto dipende dall'angolo tra la normale e la direzione della luce.
- **Far rimbalzare i raggi** ([[Raggio (Ray)]]): quando un [[Raggio (Ray)|raggio]] colpisce una superficie, la direzione del rimbalzo dipende dalla normale.
Una superficie diffusa è una superficie opaca e ruvida che sparpaglia la luce in tutte le direzioni. Pensa al muro bianco di una stanza, a un foglio di carta: non vedi riflessi specchiati, ma una luce morbida e uniforme. Questo succede perché a livello microscopico la superficie è piena di irregolarità che deviano la luce in modo casuale.

### Come rimbalza il raggio

Quando un [[Raggio (Ray)]] colpisce una superficie Lambertian, nel nostro modello semplificato facciamo così:

1. Prendiamo il punto di impatto P e la [[Le Normali|normale]] N in quel punto.
2. Generiamo una direzione casuale approssimativamente nell'emisfero sopra la superficie. Il metodo usato nel libro è: prendiamo un punto casuale sulla [[L'equazione della sfera|sfera]] unitaria centrata in P + N (cioè il punto spostato di una unità lungo la normale). La direzione dal punto di impatto verso quel punto casuale diventa la nuova direzione del [[Raggio (Ray)]].
3. Il [[Raggio (Ray)|raggio]] "rimbalza" in questa nuova direzione e continua il suo viaggio.

### Albedo

L'albedo è il colore della superficie, espresso come una terna (r, g, b) con valori tra 0 e 1. Indica quanta luce viene riflessa per ciascun canale di colore:

- Albedo (1, 0, 0) -> la superficie riflette tutta la luce rossa e assorbe verde e blu. Risultato: la superficie appare rossa.
- Albedo (0.5, 0.5, 0.5) -> riflette il 50% di ogni colore. Risultato: grigio medio.
- Albedo (1, 1, 1) -> riflette tutta la luce. Risultato: bianco.
- Albedo (0, 0, 0) -> assorbe tutta la luce. RIsultato: nero.

### Attenuation

L'attenuation è la quantità di luce che "sopravvive" dopo un rimbalzo. Nel caso Lambertian, l'attenuation coincide con l'albedo: ad ogni rimbalzo il colore del [[Raggio (Ray)|raggio]] viene moltiplicato per l'albedo della superficie.

- Dopo il 1° rimbalzo: (1·0.8, 1·0.2, 1·0.2) = (0.8, 0.2, 0.2) → rosso
- Se poi colpisce una [[L'equazione della sfera|sfera]] blu con albedo (0.2, 0.2, 0.8): (0.8·0.2, 0.2·0.2, 0.2·0.8) = (0.16, 0.04, 0.16) → molto scuro, violaceo

Ogni rimbalzo "mangia" un po' di luce. Ecco perchè le zone con molti rimbalzi (come le fessure tra due sfere) appaiono più scure: il colore si è attenuato attraverso molte moltiplicazioni.
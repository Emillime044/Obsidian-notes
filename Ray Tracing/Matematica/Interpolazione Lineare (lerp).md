L'interpolazione lineare è uno dei metodi più semplici e intuitivi per stimare un valore sconosciuto che si trova all'interno di un intervallo di dati noti.

### Come funziona

Immagina di aver pesato una pianta Lunedì (10g) e Mercoledì (20g). Se vuoi stimare quanto pesava martedì, l'interpolazione lineare assume che la crescita sia stata costante. Tracciando una linea retta tra i due dati, otterrai che Martedì pesava esattamente 15g.

### Formula

```
A=(x0​,y0​) e B=(x1​,y1​)

y=y0​ + (x − x0​) ​y1​ − y0​​
			    -------
			    x1​ − x0
```

``` (y1​−y0​)/(x1​−x0​) ```: rappresenta la pendenza della retta, quanto cambia y per ogni unità di x.
``` (x−x0​) ``` : è la distanza del tuo punto incognito dal punto di partenza.
``` y0 ​``` : è il valore base da cui parti.

### Interpolazione lineare nel ray tracing

Nel ray tracing è fondamentale per rendere le superfici realistiche senza dover gestire miliardi di poligoni. L'applicazione più celebre è l'interpolazione dei dati ai vertici

### 1. Sfumature di colore e texture

Un oggetto 3D è composto da triangoli. Se definisci un colore solo per i tre vertici di un triangolo, il software usa l'interpolazione lineare (o bilineare) per mescolare i colori dei vertici in base alla distanza del punto di impatto del [[Raggio (Ray)]] dai vertici stessi. Questo evita che l'oggetto sembri fatto di "blocchi" di colore piatto.

### 2. Lo smoothing delle Normali (phong shading)

I modelli 3D sono fatti di facce piatte, ma noi li vediamo curvi.
- Ogni vertice ha una normale ([[Le Normali]]).
- Quando  un [[Raggio (Ray)]] colpisce un punto all'interno di una faccia piatta, il computer interpola linearmente le direzioni delle normali dei vertici vicini.
- Il risultato è una finta curvatura che permette alla luce di rimbalzare in modo fluido, nascondendo i bordi netti dei poligoni.

### 3. Calcolo del punto di intesezione

Nel ray tracing, un [[Raggio (Ray)]] è una retta definita dall'equazione:

```
P(t) = O + tD
```

Dove O è l'origine (la camera) e D è la direzione. Trovare dove il raggio colpisce un oggetto significa risolvere un'equazione per trovare t. Il movimento del raggio lungo lo spazio è, di fatto, un'interpolazione lineare continua tra l'origine e un punto infinito.


### Problema

Se spari un solo raggio per pixel, il raggio passa per il centro esatto del pixel. Ma un pixel non è un puntino: è un **quadratino** che copre una piccola area della scena. Un singolo raggio può colpire il bordo di un oggetto o mancarlo di pochissimo, creando bordi "seghettati" (i famosi "scalini" o "jaggies").

### Soluzione

Per ogni pixel, spara **molti raggi** (es. 100) in posizioni leggermente diverse all'interno del quadratino del pixel — non esattamente al centro, ma in punti casuali. Poi fai la **media** di tutti i colori ottenuti:

```
colore_pixel = (colore₁ + colore₂ + ... + coloreₙ) / n)
```

### Perché funziona

Immagina un pixel al bordo di una sfera rossa su sfondo azzurro. Con un solo raggio: il pixel è o tutto rosso o tutto azzurro. Con 100 raggi: magari 60 colpiscono la sfera (rosso) e 40 lo sfondo (azzurro). La media dà un colore tra il rosso e l'azzurro - una transazione morbida che il nostro occhio percepisce come un bordo liscio.

In pratica stai campionando l'area del pixel e facendo una stima statistica del suo colore reale. Più raggi usi, più la stima è precisa. Con pochi raggi l'immagine è granulosa (il "rumore" di Monte Carlo); con molti raggi diventa liscia e pulita.
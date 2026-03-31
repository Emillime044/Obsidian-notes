### Problema: I monitor mentono

Il nostro ray tracer calcola i colori in modo "fisicamente lineare": se una superficie riflette il 50% della luce, otteniamo il valore 0.5. Il problema è che i monitor **non** mostrano i colori in modo lineare.

Se mandi il valore 0.5 a un monitor, il monitor non mostra il 50% della luminosità massima. Mostra qualcosa come il 22% (più o meno 0.5^2.2). Questo succede per ragioni storiche legate a come funzionano i tubi catodici, e lo standard è rimasto anche con i monitor moderni.

In pratica, il monitor **scurisce** tutto. I toni medi diventano troppo scuri, le ombre diventano nere, e l'immagine appare spenta e poco contrastata.

### Soluzione: sqrt(colore)

Per compensare, prima di mandare i colori al monitor applichiamo la trasformazione inversa. La versione semplificata (gamma 2.0 invece di 2.2) è:

```
colore_corretto = √(colore_lineare)
```

**Esempio:**

- Il ray tracer calcola 0.25 (un grigio abbastanza scuro in termini fisici).
- Senza correzione, il monitor lo mostra ancora più scuro (circa 0.0625).
- Con la correzione: √0.25 = 0.5, e il monitor (che scurisce) mostra circa 0.25. Il risultato è che vediamo effettivamente la luminosità che il ray tracer intendeva.

### Perché √ e non un'altra funzione

Il monitor applica all'incirca la funzione x^2.2 (chiamata "gamma del display"). Per annullarla, applichiamo la funzione inversa: x^(1/2.2). Con l'approssimazione gamma = 2 (usata nel libro per semplicità), la funzione inversa è x^(1/2) = √x.

È come indossare degli occhiali che compensano un difetto della vista: non cambiano la realtà, ma ti fanno vedere quello che c'è davvero. La sqrt non migliora i colori, li **ripristina** come dovrebbero apparire.


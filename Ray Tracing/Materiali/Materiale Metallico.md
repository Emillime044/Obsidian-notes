### La formula della riflessione

Quando un raggio colpisce uno specchio (o un metallo lucido), rimbalza in modo prevedibile. La formula è:

```
r = v − 2 · (v · N) · N
```

dove v è la direzione del raggio incidente (unitario) e N è la normale (unitaria).

### Cosa fa geometricamente — passo per passo

Immagina di lanciare una palla contro un muro. La componente della velocità perpendicolare al muro si inverte (la palla rimbalza), ma quella parallela al muro resta uguale (la palla continua a scorrere nella stessa direzione).

1. **(v · N)** — il dot product proietta v lungo la normale. Questo numero ti dice "quanta parte di v punta verso la superficie". È negativo perché v va verso la superficie ma N punta fuori (sono in direzioni opposte).
2. **(v · N) · N** — moltiplichi quel numero per la normale N. Ottieni un vettore che rappresenta la componente di v nella direzione della normale.
3. **2 · (v · N) · N** — la raddoppi. Perché non basta togliere la componente perpendicolare (otterresti un vettore che scivola lungo la superficie), devi anche aggiungerla nella direzione opposta. Togliere + aggiungere al contrario = sottrarre il doppio.
4. **v − 2·(v·N)·N** — sottrai il doppio della componente perpendicolare dal raggio originale. Il risultato è il raggio riflesso, che ha la stessa inclinazione rispetto alla normale ma dall'altra parte. Angolo di incidenza = angolo di riflessione, esattamente come dicevano a scuola.

### Fuzz

I metalli reali non sono specchi perfetti. La superficie ha microscopiche irregolarità che "sfocano" il riflesso. Il parametro **fuzz** (da 0 a 1) simula questo effetto:

- **fuzz = 0** → specchio perfetto. Il raggio riflesso è esattamente quello della formula.
- **fuzz = 0.3** → riflesso leggermente sfocato. Al raggio riflesso si aggiunge un piccolo vettore casuale (di lunghezza proporzionale a fuzz), che "disturba" la direzione.
- **fuzz = 1** → riflesso molto confuso, quasi diffuso. L'oggetto sembra satinato.
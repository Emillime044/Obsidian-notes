Un raggio è la versione matematica di "un laser che parte da un punto e va dritto in una direzione". È definito da due cose:
- Origine (punto di partenza)
- Direzione (verso dove va)

### Formula

```
P(t) = origin + t · direction
```

Questa formula fornisce qualunque punto lungo il raggio al variare di t.
Cos'è t? È un numero che dice "quanto sei avanti lungo il raggio".

Nel ray tracing, per ogni pixel dello schermo, viene sparato un raggio dalla telecamera attraverso quel pixel e si vede cosa colpisce. Trovare l'intersezione con un oggetto significa trovare il valore di t per cui il raggio tocca l'oggetto.


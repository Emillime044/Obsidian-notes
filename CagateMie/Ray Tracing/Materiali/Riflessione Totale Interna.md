### Quando succede

Guarda di nuovo la formula per |r'∥|:

```
|r'∥| = √(1 − |r'⊥|²)
```

Se |r'⊥|² > 1 significa che non esiste un [[Raggio (Ray)|raggio]] rifratto (la radice quadrata di un numero negativo non esiste nei numeri reali): tutta la luce viene riflessa indietro nel materiale, come se la superficie fosse uno specchio perfetto.

### Perché sinθ' non può essere maggiore di 1

Dalla legge di Snell ([[Rifrazione]]):

```
sin(θ') = (η / η') · sin(θ)
```

Se stai passando da un materiale denso ad uno meno denso, allora η > η', e il rapporto η/η' è maggiore di 1. Con un angolo θ abbastanza grande, il prodotto (η/η') · sin(θ) supera 1.

Ma sin(θ) non può mai essere maggiore di 1 - nessun angolo ha un seno maggiore di 1. Questo è il segnale che il [[Raggio (Ray)|raggio]] non può uscire ed è intrappolato.

### Il discriminante nel codice

Il valore sotto la radice nella formula di r'∥ funziona da discriminante:

```
discriminante = 1 − |r'⊥|²
```

- discriminante > 0 -> esiste il [[Raggio (Ray)|raggio]] rifratto, la luce passa attraverso.
- discriminante ≤ 0 -> riflessione totale interna, il materiale diventa uno specchio ([[Materiale Metallico|riflessione]]).

Nel ray tracing basta controllare questo valore: se è negativo, rifletti il [[Raggio (Ray)|raggio]] invece di rifrarlo.
### Idea

Vogliamo sapere: il [[Raggio (Ray)]] colpisce la [[L'equazione della sfera|sfera]]?

Sappiamo che:

- Un punto sul raggio è: `P(t) = O + t·d` (O = origin, D = direction)
- Un punto sulla [[L'equazione della sfera|sfera]] soddisfa: `(P - C) · (P - C) = r²`

Se un punto sta sia sulla sfera sia sul [[Raggio (Ray)]], allora possiamo sostituire P(t) al posto di P nell'equazione della sfera.

### La sostituzione

Sostituiamo `P = O + t·d` nell'equazione della [[L'equazione della sfera|sfera]]:

```
(O + t·d − C) · (O + t·d − C) = r²
```

Chiamiamo per comodità f = O - C (il [[Vettori 3D|vettore]] che va dal centro della sfera all'origine del [[Raggio (Ray)|raggio]]). L'equazione diventa:

```
(f + t·d) · (f + t·d) = r²
```

Espandiamo il dot product (funziona come il quadrato di un binomio):

```
(d · d)·t²  +  2·(f · d)·t  +  (f · f − r²)  =  0
```

### L'equazione di secondo grado

Questa è un equazione nella forma `at² + bt + c = 0` dove:

```
a = d · d             (il dot product della direzione con sé stessa)
b = 2 · (f · d)       (due volte il dot product tra f e la direzione)
c = f · f - r²        (la distanza² dall'origine al centro, meno il raggio²)
```

Le soluzioni si trovano con la classica formula:

```
t = (−b ± √(b² − 4ac)) / 2a
```

### Cosa significa il discriminante

Il discriminante è Δ = b² - 4ac, e ci dice quante volte il [[Raggio (Ray)|raggio]] incontra la sfera:

- Δ < 0 -> Nessuna soluzione reale. Il [[Raggio (Ray)|raggio]] manca la sfera completamente.
- Δ = 0 -> Una sola soluzione, il [[Raggio (Ray)|raggio]] sfiora la sfera, toccandola in un solo punto (tangente).
- Δ > 0 -> Due soluzioni, t₁ e t₂. Il [[Raggio (Ray)|raggio]] attraversa la sfera, entrando in un punto e uscendo dall'altro. In genere prendiamo la t più piccola (il punto di ingresso, cioè il più vicino alla camera), purchè t > 0.

t negativo non viene considerato perchè significa che il punto di intersezione tra il raggio e la superficie è dietro la camera.
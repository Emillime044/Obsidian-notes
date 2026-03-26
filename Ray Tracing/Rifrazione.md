Quando un [[Raggio (Ray)]] di luce passa da un materiale ad un altro, cambia direzione.

### L'indice di rifrazione

Ogni materiale ha un numero chiamato indice di rifrazione (η, "eta"), che indica quanto la luce rallenta al suo interno rispetto al vuoto:
- Vuoto/aria η ≈ 1
- Acqua η ≈ 1.33
- Vetro η ≈ 1.5
- Diamante η ≈ 2.4

Più è alto η, più il materiale "frena" la luce, e più la luce si piega quando entra.

### Legge di snell

La relazione tra l'angolo di entrata (θ) e l'angolo di uscita (θ') è:

```
η · sin(θ) = η' · sin(θ')
```

dove η è l'indice del materiale da cui proviene il [[Raggio (Ray)]], e η' è l'indice del materiale in cui entra.


### La scomposizione del [[Raggio (Ray)]] rifratto

Nel ray tracing, non usiamo sin/cos direttamente. Invece scomponiamo il [[Raggio (Ray)]] rifratto **r'** in due componenti perpendicolari tra loro:
- **r'⊥** (r perp): la componente parallela alla superficie (perpendicolare alla normale([[Le Normali]]))
- **r'∥** (r par): la componente lungo la normale([[Le Normali]]) (perpendicolare alla superficie)

Il [[Raggio (Ray)]] rifratto completo è la somma delle due:

```
r' = r'⊥ + r'∥
```

Come si calcola r'⊥

```
r'⊥ = (η / η') · (v + cos(θ) · N)
```

dove v è la direzione del [[Raggio (Ray)]] incidente (unitario) e N è la normale([[Le Normali]])  unitaria.
Il termine cos(θ) si ottiene con il dot product: cos(θ) = - (v · N) (il meno perché v punta verso la superficie, mentre N punta nella direzione opposta alla superficie). Quindi:

```
r'⊥ = (η / η') · (v + (−v · N) · N)
```

### Perché r'∥ si calcola con la radice quadrata

Il [[Raggio (Ray)]] rifratto r' deve essere unitario (lunghezza 1). Dato che r'⊥ e r'∥ sono perpendicolari, per il teorema di Pitagora:

```
|r'|² = |r'⊥|² + |r'∥|²
1     = |r'⊥|² + |r'∥|²
```

Quindi:

```
|r'∥|² = 1 − |r'⊥|²
|r'∥|  = √(1 − |r'⊥|²)
```

### Intuizione

è come un triangolo rettangolo con ipotenusa 1. Se conosci un cateto (r'⊥), l'altro cateto (r'∥) segue automaticamente da Pitagora.

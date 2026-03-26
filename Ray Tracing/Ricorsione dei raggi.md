Il cuore del ray tracing è un processo ricorsivo:
1. Spari un [[Raggio (Ray)]] dalla camera
2. Il [[Raggio (Ray)]] colpisce un oggetto -> calcoli il punto di impatto e la normale
3. Il materiale dell'oggetto decide come il [[Raggio (Ray)]] "rimbalza"
4. Un nuovo [[Raggio (Ray)]] parte dal punto di impatto nella nuova direzione
5. Ripeti dal punto 2

Ad ogni rimbalzo, il colore viene molitplicato per l'attenuation. Quando il raggio finalmente non colpisce nulla (va verso il cielo), prende il colore del cielo, e quel colore viene restituito indietro attraverso tutta la catena di rimbalzi.

### Come si accumula il colore

Immagina la catena al contrario:

```
colore_finale = attenuation₁ × attenuation₂ × ... × attenuationₙ × colore_cielo 
```

Ogni superficie moltiplica il colore per il proprio albedo. Il colore del cielo viene filtrato da ogni superficie che il [[Raggio (Ray)]] ha toccato nel suo percorso.

Esempio: un raggio rimbalza su rosso (0.8, 0, 0), poi su bianco (0.9, 0.9, 0.9), poi colpisce il cielo azzurro (0.5, 0.7, 1.0):

``` 
(0.8, 0, 0) × (0.9, 0.9, 0.9) × (0.5, 0.7, 1.0) = (0.36, 0, 0) 
```

### Perché serve un max_depth

Senza un limite, un raggio potrebbe rimbalzare all'infinito (immagina due specchi paralleli). Questo significherebbe:
- Ricorsione infinita -> il programma si blocca.
- Nessun risultato utile -> dopo molti rimbalzi il colore è praticamente nero comunque.

Il `max_depth` (tipicamente 50) dice: "dopo 50 rimbalzi, smetti e restituisci nero". In pratica, dopo 10-15 rimbalzi il contributo di colore è già trascurabile.
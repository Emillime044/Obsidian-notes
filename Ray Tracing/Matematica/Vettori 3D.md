Un vettore 3D è un gruppo di 3 numeri x, y, z.

```
v = (x, y, z)
```

Si può immaginare come una freccia nello spazio che parte dall'origine (0, 0, 0) e arriva al punto (x, y, z). In alternativa, si può pensare come uno spostamento (e.g. vai 3 passi a destra, due in alto e 1 in avanti).

Nel caso del ray tracing i vettori servono per rappresentare due cose diverse:

- **Posizioni** nello spazio (il centro di una [[L'equazione della sfera|sfera]], l'origine della camera)
- **Direzioni** (dove punta un [[Raggio (Ray)]], dove rimbalza la luce)

I numeri sono gli stessi, ma il significato cambia a seconda del contesto

## Operazioni con i vettori

### Somma

```
a + b = (a.x + b.x, a.y + b.y, a.z + b.z)
```

### Moltiplicazione per scalare

Con la moltiplicazione si allunga o si accorcia la freccia senza cambiarle la direzione. Se t=2, la freccia diventa il doppio, Se t=0.5, diventa la metà. Se t è negativo, la freccia si gira di 180°.

```
t · v = (t · v.x, t · v.y, t · v.z)
```

### Lunghezza (norma)

La lunghezza di un vettore si calcola con il teorema di Pitagora esteso a 3D.

```
|v| = √(x² + y² + z²)
```

### Normalizzazione

Normalizzare un vettore significa renderlo di lunghezza 1, mantenendo la stessa direzione. Un vettore normalizzato (detto "vettore unitario") rappresenta una direzione pura, senza informazione sulla distanza. Nel ray tracing si usano continuamente: la direzione di un [[Raggio (Ray)]], la [[Le Normali|normale]] di una superficie, ecc. Se non normalizzi, i calcoli successivi danno risultati sballati perché la lunghezza "inquina" la direzione.

```
û = v / |v|
```

### Dot Product

Il dot product misura quanto due vettori puntano nella stessa direzione.

```
a · b = a.x·b.x + a.y·b.y + a.z·b.z
```

oppure

```
a · b = |a| · |b| · cos(θ)
```

dove θ è l'angolo tra i due vettori. Questo da come risultato 3 casi:

- **a · b > 0** -> l'angolo è minore di 90°, i vettori puntano "dalla stessa parte"
- **a · b = 0** -> l'angolo è esattamente 90°, i vettori sono perpendicolari
- **a · b < 0** -> l'angolo è maggiore di 90°, puntano in "direzioni opposte"

Nel ray tracing il dot product serve a:

- Trovare le intersezioni [[Raggio (Ray)]]-[[L'equazione della sfera|sfera]] ([[Hit detection Raggio-Sfera]])
- Calcolare quanto una superficie è illuminata (più la luce è perpendicolare alla superficie, più luce riceve)
- Capire se un [[Raggio (Ray)]] colpisce il fronte o il retro di una superficie

### Cross Product

È un'operazione tra due vettori nello spazio tridimensionale che restituisce un terzo vettore perpendicolare a entrambi, il cui modulo rappresenta l'area del parallelogramma da essi formato.

```
a × b = (a.y·b.z − a.z·b.y, 
		 a.z·b.x − a.x·b.z, 
		 a.x·b.y − a.y·b.x)
```

Nel ray tracing base, il cross product non si usa molto, ma diventa essenziale quando devi costruire un sistema di coordinate locale.
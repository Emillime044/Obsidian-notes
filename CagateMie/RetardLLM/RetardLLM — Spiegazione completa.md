

Transformer character-level con NumPy, backprop manuale, trainato su Tiny Shakespeare.

---

## 0. Architettura

```
x = [18, 47, 56, ...]          (T,) indici caratteri
        │
        ▼
embedding_table[x] + positional_table[:T]
        │
        ▼
   x_embed (T, 64)             "cosa sei + dove sei"
        │
        ▼
┌─────────────────────────────────────────┐
│  Blocco b (ripetuto × 4)                │
│                                         │
│   ┌─ Self-Attention ─────────────────┐  │
│   │  Q = input @ W_q                 │  │
│   │  K = input @ W_k                 │  │
│   │  V = input @ W_v                 │  │
│   │  scores = (Q @ K.T) / √d         │  │
│   │  → causal mask → softmax → × V   │  │
│   └──────────────────────────────────┘  │
│          │                              │
│          + block_input (residual)       │
│          │                              │
│          ▼                              │
│     Layer Norm → x_norm_att, std_att    │
│          │                              │
│   ┌─ Feedforward ────────────────────┐  │
│   │  W_ff1 (64→256) → ReLU           │  │
│   │  W_ff2 (256→64)                  │  │
│   └──────────────────────────────────┘  │
│          │                              │
│          + att_normed (residual)        │
│          │                              │
│          ▼                              │
│     Layer Norm → x_norm_ff, std_ff      │
│          │                              │
│          ▼                              │
│     ff_outputs[b] → input blocco dopo   │
└─────────────────────────────────────────┘
        │
        ▼
logits = ff_output @ W_out      (T, vocab_size)
        │
        ▼
probs = softmax(logits)         (T, vocab_size)
        │
        ▼
loss = cross_entropy(probs, y)
```

---

## 1. Caricamento dati

```python
text = open("tiny_shakespeare.txt").read()
```

Carica tutto Shakespeare in una stringa.

```python
char_to_int = {}
for c in text:
    if c not in char_to_int:
        char_to_int[c] = len(char_to_int)
```

Tokenizer character-level: ogni carattere unico → un numero. Primo trovato = 0, secondo = 1, ecc.

```python
int_to_char = list(char_to_int.keys())   # numero → carattere
vocab_size = len(char_to_int)            # ~65 caratteri unici
data = np.array([char_to_int[c] for c in text])  # testo intero come array di numeri
```

---

## 2. Parametri del modello

### Embedding

```python
embedding_table  = np.random.randn(vocab_size, 64) * 0.1  # carattere → vettore
positional_table = np.random.randn(T, 64) * 0.1           # posizione → vettore
```

`embedding_table`: ogni riga è il vettore di un carattere. Il carattere 5 = riga 5.

`positional_table`: ogni riga è il vettore di una posizione. Senza questo, "ciao" e "oaic" sarebbero identici perché l'attention non sa l'ordine.

```
embedding_table[5]  = [0.12, -0.34, 0.07, ...]   ← "cosa sei"
positional_table[5] = [0.05, 0.21, -0.11, ...]   ← "dove sei"
x_embed[5]          = somma dei due               ← "cosa + dove"
```

### Pesi attention (per blocco, liste di 4)

|Variabile|Shape|Ruolo|
|---|---|---|
|`W_q[b]`|(64, 64)|Query — "cosa sto cercando?"|
|`W_k[b]`|(64, 64)|Key — "cosa contengo?"|
|`W_v[b]`|(64, 64)|Value — "cosa condivido se mi scelgono?"|

### Pesi feedforward (per blocco)

|Variabile|Shape|Ruolo|
|---|---|---|
|`W_ff1[b]`|(64, 256)|Espansione — più "spazio di lavoro"|
|`W_ff2[b]`|(256, 64)|Compressione — torna alla dimensione originale|

### Proiezione finale

|Variabile|Shape|Ruolo|
|---|---|---|
|`W_out`|(64, vocab_size)|Mappa vettori → punteggio per ogni carattere|

---

## 3. Funzioni helper

### get_batch

```python
x = data[i:i+T]       # input: T caratteri
y = data[i+1:i+T+1]   # target: stessi shiftati di 1
```

```
x: H  e  l  l  o     w  o  r  l
y: e  l  l  o     w  o  r  l  d
   ↑ ogni posizione deve predire il prossimo
```

### softmax

```python
e = exp(x - max(x))    # stabilità numerica
return e / sum(e)       # probabilità: tutte positive, sommano a 1
```

### clip_gradients

Se la norma di un gradiente supera `max_norm`, lo scala giù mantenendo la direzione. Previene l'esplosione dei gradienti.

### layer_norm

```python
x_norm = (x - mean) / std
```

Normalizza ogni riga (ogni posizione) indipendentemente. Stabilizza il training — senza questo i valori crescono o collassano attraverso i blocchi. Ritorna `x_norm` e `std` per il backprop.

### layer_norm_backward

```python
dx = (1/std) * (dout - mean(dout) - x_norm * mean(dout * x_norm))
```

Gradiente che passa indietro attraverso la layer norm. Usa `x_norm` e `std` salvati dal forward.

---

## 4. Forward pass

### Embedding

```python
x_embed = embedding_table[x] + positional_table[:len(x)]   # (T, 64)
```

Indici → vettori. Ogni carattere diventa il suo embedding + il suo positional.

### Loop dei blocchi

```python
block_input = x_embed if b == 0 else ff_outputs[b-1]
```

Blocco 0 riceve `x_embed`, gli altri ricevono l'output del blocco precedente.

### Self-Attention

```python
Q = block_input @ W_q[b]   # (T, 64) — query
K = block_input @ W_k[b]   # (T, 64) — key
V = block_input @ W_v[b]   # (T, 64) — value
```

```python
scores = (Q @ K.T) / sqrt(64)   # (T, T) — quanto i attende a j
```

Dot product tra Q e K = misura di "interesse". Diviso √64 per evitare che la softmax saturi.

```python
mask = triu(ones((T, T)), k=1)   # triangolo superiore
scores[mask == 1] = -inf         # -inf → exp(-inf) = 0 dopo softmax
```

Causal mask: la posizione i può vedere solo j ≤ i. Il modello non può barare guardando il futuro.

```
scores dopo il mask (esempio 3×3):
 0.3  -∞   -∞       1.0  0.0  0.0
 0.5  0.2  -∞   →   0.6  0.4  0.0    (dopo softmax)
 0.1  0.4  0.7      0.2  0.3  0.5
```

```python
weights = softmax(scores)            # (T, T) — att_weights
att_out = (weights @ V) + block_input  # (T, 64) — attention + residual
att_normed, att_std = layer_norm(att_out)
```

`weights @ V`: mix pesato dei value vectors — ogni posizione raccoglie info dalle posizioni passate.

`+ block_input`: connessione residuale — shortcut che aiuta il gradiente a fluire.

### Feedforward

```python
hidden = att_normed @ W_ff1[b]        # (T, 256) — espandi
hidden = maximum(0, hidden)           # ReLU — azzera i negativi
ff_out = (hidden @ W_ff2[b]) + att_normed  # (T, 64) — comprimi + residual
ff_normed, ff_std = layer_norm(ff_out)
```

MLP a due strati: espandi a 256 (più capacità), ReLU, ricomprimi a 64. Il residual `+ att_normed` è lo stesso concetto di prima.

### Proiezione finale e loss

```python
logits = ff_normed @ W_out   # (T, vocab_size) — punteggio per carattere
probs = softmax(logits)      # (T, vocab_size) — probabilità
loss = mean(-log(probs[arange(T), y]))
```

Cross entropy: prende la probabilità del carattere corretto, ne fa `-log`. Prob alta → loss bassa. Prob bassa → loss alta.

---

## 5. Backward pass

### Gradiente iniziale

```python
dlogits = probs.copy()
dlogits[arange(T), y] -= 1   # sottrai 1 al carattere corretto
dlogits /= T                  # media
```

Cross entropy + softmax combinati: prendi le prob, sottrai 1 dove c'era il target. Se il modello ha dato 0.9 al giusto → gradiente = -0.1 (piccolo). Se ha dato 0.01 → gradiente = -0.99 (grande, spinge di più).

### Proiezione finale

```python
dW_out = ff_outputs[-1].T @ dlogits   # gradiente del peso
dblock = dlogits @ W_out.T            # gradiente che va indietro
```

### Flusso nel blocco (dall'alto al basso)

```
dblock (dall'alto)
    │
    ▼
layer_norm_backward FF → dff_pre
    │
    ├── W_ff2.T → dhidden → ReLU bw → W_ff1.T ──┐
    │                                              │
    └── + dff_pre (residual FF) ──────────────────┘
    │
    ▼
datt_normed (somma dei due rami)
    │
    ▼
layer_norm_backward ATT → datt_pre
    │
    ├── attention bw → dQ, dK, dV → W_q.T, W_k.T, W_v.T ──┐
    │                                                        │
    └── + datt_pre (residual ATT) ──────────────────────────┘
    │
    ▼
dblock (verso il blocco sotto)
```

### Backprop feedforward

```python
dff_pre = layer_norm_backward(dblock, x_norm_ff[b], std_ff[b])

dW_ff2 = hiddens[b].T @ dff_pre          # grad di W_ff2
dhidden = dff_pre @ W_ff2[b].T           # grad verso hidden
dhidden = dhidden * (hiddens[b] > 0)     # ReLU: passa dove era positivo
dW_ff1 = x_norm_att[b].T @ dhidden       # grad di W_ff1
datt_normed = dhidden @ W_ff1[b].T + dff_pre   # + residual FF
```

Regola per `A @ B`: gradiente di A = `dout @ B.T`, gradiente di B = `A.T @ dout`.

Il `+ dff_pre` è il residual: nel forward `ff_out = (hidden @ W_ff2) + att_normed`, il gradiente di una somma si copia su entrambi i rami.

### Backprop attention

```python
datt_pre = layer_norm_backward(datt_normed, x_norm_att[b], std_att[b])

dweights = datt_pre @ Vs[b].T            # grad dei pesi attention
dV = att_weights[b].T @ datt_pre         # grad di V

# Softmax backward
dscores = att_weights[b] * (dweights - sum(dweights * att_weights[b], axis=1))
dscores[mask == 1] = 0                   # posizioni mascherate → 0
dscores = dscores / sqrt(64)             # scala inversa

dQ = dscores @ Ks[b]                     # grad di Q
dK = dscores.T @ Qs[b]                   # grad di K

dW_q = block_input.T @ dQ
dW_k = block_input.T @ dK
dW_v = block_input.T @ dV

dblock = dQ @ W_q[b].T + dK @ W_k[b].T + dV @ W_v[b].T + datt_pre
```

`dblock` finale: 4 contributi — Q, K, V (dal ramo attention) + `datt_pre` (residual).

### Aggiornamento pesi

```python
# Clip gradienti (max_norm = 0.5)
# Gradient descent: peso -= lr * gradiente
W_ff1[b] -= learning_rate * dW_ff1
# ... per tutti i pesi del blocco

# Fuori dal loop:
np.add.at(embedding_table, x, -learning_rate * dblock)  # solo righe usate
W_out -= learning_rate * dW_out
```

---

## 6. Generazione

```python
for _ in range(n_chars):
    context = characters[-T:]
    probs, *_ = forward_pass(np.array(context), None)
    next_char = np.random.choice(vocab_size, p=probs[-1])
    characters.append(next_char)
```

Autoregressiva: prendi gli ultimi T caratteri, forward pass, campiona dalla probabilità dell'**ultima posizione**, aggiungi al contesto, ripeti.

---

## 7. Training loop

```python
for i in range(10000):
    idx = random punto nel testo
    x, y = get_batch(data, idx, T)
    forward_pass → calcola loss
    backprop → aggiorna pesi
    ogni 100 step → stampa loss
```

**Prossimo step:** batch training — processare B sequenze alla volta. Le shape passano da `(T, 64)` a `(B, T, 64)`.
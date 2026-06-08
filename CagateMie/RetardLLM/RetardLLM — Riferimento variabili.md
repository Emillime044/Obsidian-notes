

## Pesi del modello (globali)

|Variabile|Shape|Cosa fa|
|---|---|---|
|`embedding_table`|(vocab_size, 64)|mappa ogni carattere a un vettore|
|`positional_table`|(T, 64)|mappa ogni posizione a un vettore|
|`W_q[b]`|(64, 64)|proietta in query — "cosa sto cercando?"|
|`W_k[b]`|(64, 64)|proietta in key — "cosa contengo?"|
|`W_v[b]`|(64, 64)|proietta in value — "cosa condivido?"|
|`W_ff1[b]`|(64, 256)|feedforward espansione|
|`W_ff2[b]`|(256, 64)|feedforward compressione|
|`W_out`|(64, vocab_size)|proiezione finale → logits|

## Cache del forward pass (per blocco, indicizzate con [b])

| Variabile        | Shape    | Cosa fa                                                                     |
| ---------------- | -------- | --------------------------------------------------------------------------- |
| `Qs[b]`          | (T, 64)  | query = block_input @ W_q                                                   |
| `Ks[b]`          | (T, 64)  | key = block_input @ W_k                                                     |
| `Vs[b]`          | (T, 64)  | value = block_input @ W_v                                                   |
| `att_weights[b]` | (T, T)   | pesi attention dopo softmax — quanto ogni posizione attende alle altre      |
| `hiddens[b]`     | (T, 256) | output del feedforward dopo ReLU (prima di W_ff2)                           |
| `ff_outputs[b]`  | (T, 64)  | output finale del blocco (dopo layer norm FF) = input del blocco successivo |
| `x_norm_att[b]`  | (T, 64)  | output normalizzato della layer norm dopo attention                         |
| `std_att[b]`     | (T, 1)   | deviazione standard della layer norm dopo attention                         |
| `x_norm_ff[b]`   | (T, 64)  | output normalizzato della layer norm dopo feedforward                       |
| `std_ff[b]`      | (T, 1)   | deviazione standard della layer norm dopo feedforward                       |

## Altre variabili del forward

|Variabile|Shape|Cosa fa|
|---|---|---|
|`x_embed`|(T, 64)|embedding + positional encoding — input al primo blocco|
|`mask`|(T, T)|triangolo superiore di 1 — posizioni future da mascherare|
|`probs`|(T, vocab_size)|probabilità finali su tutto il vocabolario|
|`loss`|scalare|cross entropy media su tutte le posizioni|

## Gradienti nel backprop

|Variabile|Cosa fa|
|---|---|
|`dlogits`|gradiente iniziale dalla loss (softmax + cross entropy)|
|`dW_out`|gradiente di W_out|
|`dblock`|gradiente che scorre da blocco a blocco — entra dalla cima e scende|
|`dff_pre`|gradiente dopo backprop della layer norm FF (prima del residual FF)|
|`dhidden`|gradiente dell'hidden layer del feedforward|
|`datt_normed`|gradiente che entra nella layer norm attention (include residual FF)|
|`datt_pre`|gradiente dopo backprop della layer norm attention (prima del residual ATT)|
|`dweights`|gradiente dei pesi attention|
|`dscores`|gradiente degli score attention (dopo backprop softmax)|
|`dQ, dK, dV`|gradienti delle proiezioni query, key, value|
|`dW_q, dW_k, dW_v`|gradienti dei pesi attention|
|`dW_ff1, dW_ff2`|gradienti dei pesi feedforward|

## Flusso del backprop in un blocco

```
dblock (dall'alto)
    │
    ▼
layer_norm_backward FF → dff_pre
    │
    ├── W_ff2.T → dhidden → ReLU backward → W_ff1.T ──┐
    │                                                   │
    └── residual FF ────────────────────────────────────┘
    │
    ▼
datt_normed (somma dei due rami)
    │
    ▼
layer_norm_backward ATT → datt_pre
    │
    ├── attention backward → dQ, dK, dV → W_q.T, W_k.T, W_v.T ────┐
    │                                                             │
    └── residual ATT ─────────────────────────────────────────────┘
    │
    ▼
dblock (verso il blocco sotto)
```
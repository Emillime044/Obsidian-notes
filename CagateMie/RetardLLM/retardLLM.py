import numpy as np

# ============================================================
# Iperparametri
# ============================================================
embed_dim = 64
T = 128
learning_rate = 0.001
epsilon = 1e-5
n_blocks = 4

global W_q, W_k, W_v, W_ff1, W_ff2, W_out, positional_table, embedding_table

# ============================================================
# Caricamento dati
# ============================================================
text = open("tiny_shakespeare.txt").read()

char_to_int = {}
for c in text:
    if c not in char_to_int:
        char_to_int[c] = len(char_to_int)

int_to_char = list(char_to_int.keys())
vocab_size = len(char_to_int)
data = np.array([char_to_int[c] for c in text])

# ============================================================
# Parametri del modello
# ============================================================
embedding_table  = np.random.randn(vocab_size, embed_dim) * 0.1
positional_table = np.random.randn(T, embed_dim) * 0.1

W_q   = [np.random.randn(embed_dim, embed_dim) * 0.1 for _ in range(n_blocks)]
W_k   = [np.random.randn(embed_dim, embed_dim) * 0.1 for _ in range(n_blocks)]
W_v   = [np.random.randn(embed_dim, embed_dim) * 0.1 for _ in range(n_blocks)]
W_ff1 = [np.random.randn(embed_dim, embed_dim * 4) * 0.1 for _ in range(n_blocks)]
W_ff2 = [np.random.randn(embed_dim * 4, embed_dim) * 0.1 for _ in range(n_blocks)]
W_out = np.random.randn(embed_dim, vocab_size) * 0.01

# ============================================================
# Funzioni helper
# ============================================================
def get_batch(data, i, T):
    x = data[i:i+T]
    y = data[i+1:i+T+1]
    return x, y

def softmax(x):
    e = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e / np.sum(e, axis=1, keepdims=True)

def clip_gradients(gradients, max_norm):
    clipped = []
    for grad in gradients:
        norm = np.linalg.norm(grad)
        if norm > max_norm:
            grad = grad * (max_norm / norm)
        clipped.append(grad)
    return clipped

def layer_norm(x):
    mean = np.mean(x, axis=-1, keepdims=True)
    std = np.sqrt(np.var(x, axis=-1, keepdims=True) + epsilon)
    x_norm = (x - mean) / std
    return x_norm, std

def layernorm_backward(dout, x_norm, std):
    dx = (1/std) * (dout - np.mean(dout, axis=-1, keepdims=True) - x_norm * np.mean(dout * x_norm, axis=-1, keepdims=True))
    return dx

def generate(start_char, n_chars):
    characters = [char_to_int[start_char]]
    for _ in range(n_chars):
        context = characters[-T:]
        probs, ff_outputs, hiddens, weightss, mask, x_embed, loss, outputs, Vs, Qs, Ks, stds_att, stds_ff = forward_pass(np.array(context), None)
        next_char = np.random.choice(vocab_size, p=probs[-1])
        characters.append(next_char)
    print(''.join([int_to_char[i] for i in characters]))

# ============================================================
# Forward pass
# ============================================================
def forward_pass(x, y):
    global W_q, W_k, W_v, W_ff1, W_ff2, W_out, positional_table, embedding_table
    Qs, Ks, Vs, weightss, outputs, hiddens, ff_outputs, stds_att, stds_ff = [], [], [], [], [], [], [], [], []
    x_embed = embedding_table[x] + positional_table[:len(x)]

    for b in range(n_blocks):
        block_input = x_embed if b == 0 else ff_outputs[b-1]

        Q = block_input @ W_q[b]
        Qs.append(Q)
        K = block_input @ W_k[b]
        Ks.append(K)
        V = block_input @ W_v[b]
        Vs.append(V)

        scores = Q @ K.T / np.sqrt(embed_dim)
        seq_len = len(x)
        mask = np.triu(np.ones((seq_len, seq_len)), k=1)
        scores[mask == 1] = -np.inf

        weights = softmax(scores)
        weightss.append(weights)

        output, std_att = layer_norm((weights @ V) + block_input)
        outputs.append(output)
        stds_att.append(std_att)

        hidden = output @ W_ff1[b]
        hidden = np.maximum(0, hidden)
        hiddens.append(hidden)

        ff_output = hidden @ W_ff2[b]
        ff_output, std_ff = layer_norm(ff_output + output)
        ff_outputs.append(ff_output)
        stds_ff.append(std_ff)

    logits = ff_output @ W_out
    probs = softmax(logits)

    if y is not None:
        loss = np.mean(-np.log(probs[np.arange(T), y]))
    else:
        loss = None

    return probs, ff_outputs, hiddens, weightss, mask, x_embed, loss, outputs, Vs, Qs, Ks, stds_att, stds_ff

# ============================================================
# Backprop
# ============================================================
def backprop(probs, ff_outputs, hiddens, weightss, mask, x_embed, loss, outputs, Vs, Qs, Ks, stds_att, stds_ff, x, y):
    global W_q, W_k, W_v, W_ff1, W_ff2, W_out, positional_table, embedding_table

    dlogits = probs.copy()
    dlogits[np.arange(T), y] -= 1
    dlogits /= T

    dW_out = ff_outputs[-1].T @ dlogits
    dff_output = dlogits @ W_out.T

    for b in range(n_blocks-1, -1, -1):
        block_input = x_embed if b == 0 else ff_outputs[b-1]

        # layer norm backward feedforward
        dff_output = layernorm_backward(dff_output, ff_outputs[b], stds_ff[b])

        # feedforward backward
        dW_ff2      = hiddens[b].T @ dff_output
        dhidden     = dff_output @ W_ff2[b].T
        dhidden     = dhidden * (hiddens[b] > 0)
        dW_ff1      = outputs[b].T @ dhidden
        datt_output = dhidden @ W_ff1[b].T + dff_output

        # layer norm backward attention
        datt_output = layernorm_backward(datt_output, outputs[b], stds_att[b])

        # attention backward
        dweights = datt_output @ Vs[b].T
        dV       = weightss[b].T @ datt_output

        dscores = weightss[b] * (dweights - np.sum(dweights * weightss[b], axis=1, keepdims=True))
        dscores[mask == 1] = 0
        dscores = dscores / np.sqrt(embed_dim)

        dQ = dscores @ Ks[b]
        dK = dscores.T @ Qs[b]

        dW_q = block_input.T @ dQ
        dW_k = block_input.T @ dK
        dW_v = block_input.T @ dV

        dx_embed  = dQ @ W_q[b].T
        dx_embed += dK @ W_k[b].T
        dx_embed += dV @ W_v[b].T

        dff_output = dx_embed + datt_output

        dW_q, dW_k, dW_v, dW_ff1, dW_ff2, dW_out, dx_embed = clip_gradients(
            [dW_q, dW_k, dW_v, dW_ff1, dW_ff2, dW_out, dx_embed], max_norm=1.0)

        W_ff1[b] -= learning_rate * dW_ff1
        W_ff2[b] -= learning_rate * dW_ff2
        W_q[b]   -= learning_rate * dW_q
        W_k[b]   -= learning_rate * dW_k
        W_v[b]   -= learning_rate * dW_v
        positional_table -= learning_rate * dx_embed

    np.add.at(embedding_table, x, -learning_rate * dx_embed)
    W_out -= learning_rate * dW_out

# ============================================================
# Training loop
# ============================================================
for i in range(10000):
    idx = np.random.randint(0, len(data) - T - 1)
    x, y = get_batch(data, idx, T)
    probs, ff_outputs, hiddens, weightss, mask, x_embed, loss, outputs, Vs, Qs, Ks, stds_att, stds_ff = forward_pass(x, y)
    backprop(probs, ff_outputs, hiddens, weightss, mask, x_embed, loss, outputs, Vs, Qs, Ks, stds_att, stds_ff, x, y)
    if i % 100 == 0:
        print(loss)

generate('A', 200)
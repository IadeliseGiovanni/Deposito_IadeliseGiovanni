import numpy as np

# 1. CREAZIONE E ISPEZIONE
parte1 = np.arange(50) # Crea array da 0 a 49
parte2 = np.random.randint(49, 101, 50) # 50 numeri casuali tra 49 e 101
arr = np.concatenate([parte1, parte2])
info_iniziale = (arr.dtype, arr.shape)

# 2. MODIFICA TIPO
arr = arr.astype('float64') # Converte in float64
info_post_conv = (arr.dtype, arr.shape)

# 3. SLICING (Estrazione sotto-array)
p10 = arr[:10]   # Primi 10
u7 = arr[-7:]    # Ultimi 7
r5_20 = arr[5:20] # Da indice 5 a 20 (escluso)
ogni_4 = arr[::4] # Ogni quarto elemento

# 4. MODIFICA TRAMITE SLICING
arr[10:15] = 999 # Assegna 999 agli indici 10-14

# 5. FANCY INDEXING E MASCHERE BOOLEANE
fancy = arr[[0, 3, 7, 12, 25, 33, 48]] # Indici specifici
pari = arr[arr % 2 == 0] # Filtro numeri pari
sopra_media = arr[arr > arr.mean()] # Filtro sopra la media

# --- TUTTI I PRINT ALLA FINE ---
print("=== REPORT FINALE ESERCIZIO ===")
print(f"1. Inizio - Dtype: {info_iniziale[0]}, Shape: {info_iniziale[1]}")
print(f"2. Dopo conversione - Dtype: {info_post_conv[0]}, Shape: {info_post_conv[1]}")
print("-" * 30)
print(f"3. Slicing Primi 10: {p10}")
print(f"3. Slicing Ultimi 7: {u7}")
print(f"3. Slicing Range 5-20: {r5_20}")
print(f"3. Ogni quarto elemento: {ogni_4}")
print("-" * 30)
print(f"4. Array con modifica 999 (prime 20 posizioni): {arr[:20]}")
print("-" * 30)
print(f"5. Fancy Indexing (posizioni scelte): {fancy}")
print(f"5. Numeri Pari trovati: {len(pari)}")
print(f"5. Numeri Sopra la Media trovati: {len(sopra_media)}")
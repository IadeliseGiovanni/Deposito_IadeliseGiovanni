import numpy as np

#              --- ESERCIZIO 1: Somma e Media di Elementi ---
# 1. Creare un array NumPy di 15 elementi contenente numeri casuali tra 1 e 100
array_es1 = np.random.randint(1, 101, 15)

# 2. Calcolare e stampare la somma di tutti gli elementi dell'array
somma_es1 = array_es1.sum() 

# 3. Calcolare e stampare la media di tutti gli elementi dell'array
media_es1 = array_es1.mean()

print(f"Es 1 - Array: {array_es1}")
print(f"Es 1 - Somma: {somma_es1}, Media: {media_es1:.2f}\n")


#          --- ESERCIZIO 2: Manipolazione di Array Multidimensionali ---
# 1. Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25
matrice_5x5 = np.arange(1, 26).reshape(5, 5)

# 2. Estrarre e stampare la seconda colonna della matrice
seconda_colonna = matrice_5x5[:, 1]

# 3. Estrarre e stampare la terza riga della matrice
terza_riga = matrice_5x5[2, :]

# 4. Calcolare e stampare la somma degli elementi della diagonale principale
somma_diagonale = np.diag(matrice_5x5).sum()

print(f"Es 2 - Matrice:\n{matrice_5x5}")
print(f"Es 2 - Seconda Colonna: {seconda_colonna}")
print(f"Es 2 - Terza Riga: {terza_riga}")
print(f"Es 2 - Somma Diagonale: {somma_diagonale}\n")


#         --- ESERCIZIO 3: Operazioni con Fancy Indexing ---
# 1. Creare un array NumPy di forma (4, 4) con numeri casuali tra 10 e 50
arr_fancy = np.random.randint(10, 51, size=(4, 4))

# 2. Fancy indexing per selezionare elementi (0, 1), (1, 3), (2, 2) e (3, 0)
elementi_fnd = arr_fancy[[0, 1, 2, 3], [1, 3, 2, 0]]

# 3. Fancy indexing per selezionare tutte le righe dispari (indice 1 e 3)
righe_dispari = arr_fancy[[1, 3], :]

# 4. Modificare gli elementi del punto 2 aggiungendo 10 al loro valore
arr_fancy[[0, 1, 2, 3], [1, 3, 2, 0]] += 10

print(f"Es 3 - Matrice Fancy Originale (modificata):\n{arr_fancy}")
print(f"Es 3 - Righe Dispari:\n{righe_dispari}\n")


# --- SISTEMA FINALE: GESTIONE MATRICE 2D (Parte 1, 2 ed EXTRA) ---
def sistema_interattivo():
    # 1. Creare una nuova matrice 2D di dimensioni specificate dall'utente (Parte UNO)
    r = int(input("Inserisci righe per la matrice finale: "))
    c = int(input("Inserisci colonne per la matrice finale: "))
    matrice = np.random.randint(1, 10, size=(r, c))
    
    # 2. Estrarre e stampare la sotto-matrice centrale (Parte UNO)
    if r > 2 and c > 2:
        centrale = matrice[1:-1, 1:-1]
        print(f"Sotto-matrice centrale:\n{centrale}")
    
    # 3. Trasporre la matrice e stamparla (Parte UNO)
    trasposta = matrice.T
    print(f"Matrice Trasposta:\n{trasposta}")
    
    # 4. Calcolare e stampare la somma di tutti gli elementi (Parte UNO)
    print(f"Somma totale elementi: {matrice.sum()}")
    
    # 6. Moltiplicazione Element-wise con un'altra Matrice (Parte DUE)
    matrice2 = np.random.randint(1, 10, size=matrice.shape)
    moltiplicazione = matrice * matrice2
    print(f"Risultato Moltiplicazione Element-wise:\n{moltiplicazione}")
    
    # 7. Calcolo della Media degli Elementi (Parte DUE)
    print(f"Media della matrice: {np.mean(matrice):.2f}")
    
    # EXTRA: Determinante della Matrice (solo se quadrata)
    if r == c:
        print(f"Determinante: {np.linalg.det(matrice):.2f}")

# Esegui il sistema finale
sistema_interattivo()
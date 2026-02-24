#ESERCIZIO 1

import numpy as np

# 1. Crea un array di 15 elementi con numeri casuali tra 1 e 100
# Usiamo randint(min, max, quanti)
array_es1 = np.random.randint(1, 101, 15)

# 2. Calcola la somma di tutti gli elementi
somma_totale = array_es1.sum()

# 3. Calcola la media di tutti gli elementi
media_totale = array_es1.mean()

print("--- ESERCIZIO 1 ---")
print(f"Array generato: {array_es1}")
print(f"Somma totale: {somma_totale}")
print(f"Media totale: {media_totale:.2f}")


#ESERCIZIO 2

import numpy as np

# 1. Crea una matrice 5x5 con numeri sequenziali da 1 a 25
# Usiamo arange per i numeri e reshape per dargli la forma 5x5
matrice_5x5 = np.arange(1, 26).reshape(5, 5)

# 2. Estrai e stampa la SECONDA COLONNA
# Sintassi [tutte le righe, colonna indice 1]
seconda_colonna = matrice_5x5[:, 1]

# 3. Estrai e stampa la TERZA RIGA
# Sintassi [riga indice 2, tutte le colonne]
terza_riga = matrice_5x5[2, :]

# 4. Calcola la somma degli elementi della diagonale principale
somma_diagonale = np.diag(matrice_5x5).sum()

print("\n--- ESERCIZIO 2 ---")
print(f"Matrice 5x5 completa:\n{matrice_5x5}")
print(f"Seconda colonna: {seconda_colonna}")
print(f"Terza riga: {terza_riga}")
print(f"Somma diagonale principale: {somma_diagonale}")



#ESERCIZIO 3 


import numpy as np

# 1. Crea un array di forma (4, 4) con numeri casuali interi tra 10 e 50
arr = np.random.randint(10, 51, size=(4, 4))

# 2. Utilizza fancy indexing per selezionare elementi a indici specifici:
# (0, 1), (1, 3), (2, 2) e (3, 0)
# Passiamo una lista per le righe e una per le colonne
indici_righe = [0, 1, 2, 3]
indici_colonne = [1, 3, 2, 0]
elementi_selezionati = arr[indici_righe, indici_colonne]

# 3. Utilizza fancy indexing per selezionare tutte le righe dispari
# (Considerando la numerazione che parte da 0: riga 1 e riga 3)
righe_dispari = arr[[1, 3], :]

# 4. Modifica gli elementi del punto 2 aggiungendo 10 al loro valore
arr[indici_righe, indici_colonne] += 10

print("--- ESERCIZIO 3 ---")
print(f"Matrice originale:\n{arr - 10}") # (Mostro l'originale sottraendo quello che ho aggiunto dopo)
print(f"\nElementi selezionati al punto 2: {elementi_selezionati}")
print(f"\nMatrice con righe dispari:\n{righe_dispari}")
print(f"\nMatrice finale (dopo aver aggiunto 10 ai punti specifici):\n{arr}")
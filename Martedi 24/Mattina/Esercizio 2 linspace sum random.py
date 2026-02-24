import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace
array_lin = np.linspace(0, 1, 12)

# 2. Cambia la forma dell'array a una matrice 3x4
matrice_A = array_lin.reshape(3, 4)

# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1
matrice_B = np.random.rand(3, 4)

# 4. Calcola la somma degli elementi di entrambe le matrici
somma_A = matrice_A.sum()
somma_B = matrice_B.sum()

# Stampa dei risultati
print("=== MATRICE A (Linspace) ===")
print(matrice_A)
print(f"Somma elementi Matrice A: {somma_A:.2f}\n")

print("=== MATRICE B (Casuale) ===")
print(matrice_B)
print(f"Somma elementi Matrice B: {somma_B:.2f}")
import numpy as np
import os

def esegui_esercizio():
    while True:
        # 1. Utilizza np.linspace per creare un array di 50 numeri tra 0 e 10
        array_lin = np.linspace(0, 10, 50) #

        # 2. Utilizza np.random.random per 50 numeri casuali tra 0 e 1
        array_rand = np.random.random(50) #

        # 3. Somma i due array elemento per elemento (operazione vettoriale)
        nuovo_array = array_lin + array_rand #

        # 4. Calcola la somma totale
        somma_totale = nuovo_array.sum() #

        # 5. Calcola la somma degli elementi > 5 (filtro booleano)
        somma_maggiori_5 = nuovo_array[nuovo_array > 5].sum() #

        # 6. Stampa i risultati a video
        print("\n--- RISULTATI ---")
        print(f"Somma totale: {somma_totale:.2f}")
        print(f"Somma elementi > 5: {somma_maggiori_5:.2f}")

        # 7, 8, 9. Gestione salvataggio su file TXT
        nome_file = "risultati_numpy.txt"
        
        # Chiedi se sovrascrivere o aggiungere
        scelta_file = input(f"\nVuoi sovrascrivere il file {nome_file}? (si/no): ").lower()
        modo_apertura = 'w' if scelta_file == 's' else 'a'

        with open(nome_file, modo_apertura) as f:
            f.write(f"Somma Totale: {somma_totale}\n")
            f.write(f"Somma > 5: {somma_maggiori_5}\n")
            f.write("-" * 20 + "\n")
        
        print(f"Dati salvati in {nome_file} con successo!")

        # Chiedi se ripetere il processo
        ripeti = input("\nVuoi ripetere l'intero processo? (si/no): ").lower()
        if ripeti != 's':
            print("Esercizio terminato. Ciao!")
            break

# Avvia l'esercizio
esegui_esercizio()
import numpy as np

# 1. Creazione di un segnale
# Generiamo 400 punti equidistanti tra 0 e 1 per rappresentare il tempo (t)
t = np.linspace(0, 1, 400) 

# Creiamo un segnale composto dalla somma di due onde sinusoidali (50Hz e 120Hz)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# 2. Calcolo della Trasformata di Fourier
# Questa funzione scompone il segnale nelle sue frequenze componenti
fft_sig = np.fft.fft(sig)

# 3. Calcolo delle frequenze associate
# Restituisce i valori delle frequenze corrispondenti ai risultati della FFT
freqs = np.fft.fftfreq(len(fft_sig))

# STAMPA DEI RISULTATI
# Nota: La FFT produce numeri complessi (con la parte 'j')
print("--- TRASFORMATA DI FOURIER (Primi 5 valori) ---")
print(fft_sig[:5]) 

print("\n--- FREQUENZE ASSOCIATE (Primi 5 valori) ---")
print(freqs[:5])
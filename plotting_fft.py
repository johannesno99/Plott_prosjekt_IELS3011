import matplotlib.pyplot as plt
import numpy as np

# Lese filen
with open("x-fft.txt", "r") as f:
    lines = f.readlines()

# Konvertere linjer til flyttall, håndtere både punktum og komma som desimaltegn
Values = [float(line.strip().replace(",", ".")) for line in lines if line.strip()]

# Generere x-verdier fra 0 til 500 Hz
x_values = np.linspace(0, 500, len(Values))

# Plotte data
plt.figure(figsize=(10, 5))
plt.plot(x_values, Values, marker="o", linestyle="-", color="orange")
plt.title("FFT av vibrasjonsdata")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)
plt.xlim(0, 500)
plt.show()

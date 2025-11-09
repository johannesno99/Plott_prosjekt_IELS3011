import matplotlib.pyplot as plt

# Lese filen
with open("x-g.txt", "r") as f:
    lines = f.readlines()

# Konvertere linjer til flyttall, håndtere både punktum og komma som desimaltegn
values = [float(line.strip().replace(",", ".")) for line in lines if line.strip()]

# Lage en x - rad for målingene 
x_values = list(range(1, len(values) + 1))

# Finne maks- og minverdier
max_val = max(values)
min_val = min(values)
max_index = values.index(max_val)
min_index = values.index(min_val)

# Plott data
plt.figure(figsize=(10, 5))
plt.plot(x_values, values, marker="o", linestyle="-", color="grey", label="g-data")

# Marker maks og min i plottet
plt.scatter(max_index + 1, max_val, color="red", label=f"Maks: {max_val:.3f}")
plt.scatter(min_index + 1, min_val, color="blue", label=f"Min: {min_val:.3f}")

# Tekst-annotasjoner på punktene
plt.text(max_index + 1, max_val, f"  {max_val:.3f}", color="red", va="bottom")
plt.text(min_index + 1, min_val, f"  {min_val:.3f}", color="blue", va="top")

# Formatering av graf
plt.title("Plotting av g-data med maks og min verdier")
plt.xlabel("Målepunkter")
plt.ylabel("Amplitude (g)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

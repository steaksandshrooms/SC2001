#c(ii), n fixed, S varies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from hybridsort import hybrid_mergesort

# Parameters
n = 1000
num_trials = 5
thresholds = range(2, 100)

# Collect data
data = []
for t in thresholds:
    comparisons_hybrid = []
    for _ in range(num_trials):
        arr = np.random.randint(1, n+1, size=n).tolist()
        ch, _ = hybrid_mergesort(arr[:], t)   # the actual function
        comparisons_hybrid.append(ch)
    
    avg_ch = np.mean(comparisons_hybrid)
    
    # Theoretical formula
    T = (n * t) / 4 + n * np.log2(n / t) - (n / t) - (n / 2) + 1
    
    data.append({"Threshold": t, "Hybrid Comparisons": avg_ch, "Theoretical": T})

# Convert to DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# ==== Plot ====
plt.figure(figsize=(10, 6))
plt.plot(df["Threshold"], df["Hybrid Comparisons"], linestyle="-", label="Hybrid Merge-Insertion Sort")
plt.plot(df["Threshold"], df["Theoretical"], linestyle=":", color="green", label="Theoretical Formula")

plt.xlabel("Threshold (S)")
plt.ylabel("Average # of Comparisons")
plt.title(f"Hybrid Comparisons vs Theoretical (n={n}, {num_trials} trials)")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.show()
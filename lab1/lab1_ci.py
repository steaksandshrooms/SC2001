# experiment_c_i.py
# Part (c)(i): Hybrid mergesort comparisons vs n with S=12, 3 runs per size, theoretical line

import random
import math
import matplotlib.pyplot as plt

# Import the hybrid algorithm
from hybridsort import hybrid_mergesort  # counts comparisons and returns (comparisons, sorted_list)

# Use the exact size values from dataset.py (avoid importing to prevent side effects)
# dataset.py defines: size_list = [1000, 2000, 5000, 10000, 20000, 50000, 100000,
#                                  200000, 500000, 1000000, 2000000, 5000000, 10000000]
SIZE_LIST = [1000, 2000, 5000, 10000, 20000, 50000, 100000,
             200000, 500000, 1000000, 2000000, 5000000, 10000000]

# Largest integer value used in dataset.py for random generation
X_MAX = 10**6

# Configuration per c(i)
S = 12
TRIALS = 3

def run_experiment():
    rng = random.Random(42)  # reproducibility
    n_values = []
    avg_comparisons = []

    for n in SIZE_LIST:
        # Generate one random array for this n as in dataset.py
        base_arr = [rng.randint(1, X_MAX) for _ in range(n)]

        # Run the same array 3 times (on copies), record #comparisons
        comps = []
        for _ in range(TRIALS):
            c, sorted_arr = hybrid_mergesort(list(base_arr), S=S)
            comps.append(c)

        avg_c = sum(comps) / TRIALS
        n_values.append(n)
        avg_comparisons.append(avg_c)
        print(f"n={n:,}, trials={TRIALS}, avg comparisons={avg_c:,.0f}")

    return n_values, avg_comparisons

def theoretical_curve(n_values, empirical):
    # Normalize theoretical nlog_2(n) to the first empirical point to make both curves comparable on the same scale
    def f(n): 
        return n * math.log2(n)

    # Avoid n=1; for given sizes, n >= 1000 so safe
    scale = empirical[0] / f(n_values[0])
    theo = [scale * f(n) for n in n_values]
    return theo

if __name__ == "__main__":
    n_vals, avg_comps = run_experiment()
    theo_vals = theoretical_curve(n_vals, avg_comps)

    plt.figure(figsize=(9, 6))
    plt.plot(n_vals, avg_comps, marker="o", linewidth=2, label="Hybrid empirical (S=12)")
    plt.plot(n_vals, theo_vals, linestyle="--", linewidth=2, label="Theoretical ~ n·log_2(n)")
    plt.yticks(np.arange(0, 3, 1))
    plt.xlabel("Array size n")
    plt.ylabel("Number of comparisons")
    plt.title("Hybrid mergesort comparisons vs n (S=12)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

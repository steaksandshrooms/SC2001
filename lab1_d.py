import time
import numpy as np
import matplotlib.pyplot as plt

from hybridsort import hybrid_mergesort as hybridmergesort, pure_mergesort as puremergesort

try:
    from lab1_ciii import findoptimals
except ImportError:
    findoptimals = None


def partd():
    # Project Part (d) parameters
    N = 10_000_000       # dataset size
    XMAX = 1_000_000     # value range upper bound

    # Obtain optimal S from part (c-iii) if available, else fall back to a sane default
    if findoptimals is not None:
        S_opt = findoptimals()
    else:
        S_opt = 12  # fallback if part (c-iii) function is not importable

    print(f"Using S = {S_opt}")

    # Generate dataset
    rng = np.random.default_rng(42)
    base = rng.integers(1, XMAX + 1, size=N, dtype=np.int64).tolist()

    # Run hybrid sort
    print("Running hybrid sort...")
    t0_wall = time.perf_counter()
    t0_cpu = time.process_time()
    h_comparisons, h_sorted = hybridmergesort(base.copy(), S_opt)
    h_wall = time.perf_counter() - t0_wall
    h_cpu = time.process_time() - t0_cpu

    # Run pure mergesort
    print("Running pure mergesort...")
    t0_wall = time.perf_counter()
    t0_cpu = time.process_time()
    p_comparisons, p_sorted = puremergesort(base.copy())
    p_wall = time.perf_counter() - t0_wall
    p_cpu = time.process_time() - t0_cpu

    # Report results
    print(f"Hybrid (S={S_opt}): comparisons={h_comparisons:,}, wall={h_wall:.3f}s, cpu={h_cpu:.3f}s")
    print(f"Pure mergesort: comparisons={p_comparisons:,}, wall={p_wall:.3f}s, cpu={p_cpu:.3f}s")
    
    faster = "Hybrid" if h_wall < p_wall else "Pure mergesort"
    print(f"Faster by wall time: {faster}")
    
    # Generate bar graphs
    print("\nGenerating bar graphs...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Prepare data
    algorithms = [f"Hybrid (S={S_opt})", "Pure mergesort"]
    comparisons = [h_comparisons, p_comparisons]
    cpu_times = [h_cpu, p_cpu]
    
    # Convert to scientific notation for display
    comparisons_sci = [comp / 1e8 for comp in comparisons]  # Scale to 1e8 units
    
    # Bar graph 1: Number of Comparisons
    bars1 = ax1.bar(algorithms, comparisons_sci, color=['#1f77b4', '#d62728'], alpha=0.8)
    ax1.set_title(f'Number of Comparisons (n={N:,})', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Comparisons', fontsize=12)
    ax1.set_ylim(0, max(comparisons_sci) * 1.1)
    
    # Format y-axis to show 1e8 scale
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}'))
    ax1.tick_params(axis='y', labelsize=10)
    ax1.tick_params(axis='x', labelsize=10)
    
    # Add value labels on bars
    for bar, value in zip(bars1, comparisons_sci):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'{value:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Bar graph 2: CPU Time
    bars2 = ax2.bar(algorithms, cpu_times, color=['#1f77b4', '#d62728'], alpha=0.8)
    ax2.set_title(f'CPU Time (n={N:,})', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Seconds', fontsize=12)
    ax2.set_ylim(0, max(cpu_times) * 1.1)
    
    # Add value labels on bars
    for bar, value in zip(bars2, cpu_times):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'{value:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Style the plots
    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.3, axis='y')
        ax.set_axisbelow(True)
    
    plt.tight_layout()
    plt.savefig('sorting_comparison_bar_graphs.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\nGraph saved as:")
    print("- sorting_comparison_bar_graphs.png")


if __name__ == "__main__":
    partd()

import time
import numpy as np
import matplotlib.pyplot as plt

from hybridsort import hybrid_mergesort , pure_mergesort 
from dataset import datasets
from lab1_ciii import find_optimal_s

def partd():
    print("Starting partd() function...")
    N = 10_000_000     
    print(f"Requested dataset size: {N}")
    print("Finding optimal S...")
    S = find_optimal_s()
    print(f"Using S = {S}")
    
    if N in datasets:
        base = datasets[N].copy()
        print(f"Using dataset from dataset.py with size {N}")
    else:
        print(f"Dataset size {N} not found in dataset.py, using largest available dataset")
        largest_size = max(datasets.keys())
        base = datasets[largest_size].copy()
        N = largest_size
        print(f"Using dataset with size {N}")
  
    print("Running hybrid sort...")
    t0_wall = time.perf_counter()
    t0_cpu = time.process_time()
    hcomparisons, hsorted = hybrid_mergesort(base.copy(), S)
    hwall = time.perf_counter() - t0_wall
    hcpu = time.process_time() - t0_cpu

    print("Running pure mergesort...")
    t0_wall = time.perf_counter()
    t0_cpu = time.process_time()
    pcomparisons, psorted = pure_mergesort(base.copy())
    pwall = time.perf_counter() - t0_wall
    pcpu = time.process_time() - t0_cpu

    print(f"Hybrid (S={S}): comparisons={hcomparisons:,}, wall={hwall:.3f}s, cpu={hcpu:.3f}s")
    print(f"Pure mergesort: comparisons={pcomparisons:,}, wall={pwall:.3f}s, cpu={pcpu:.3f}s")
    
    faster = "Hybrid" if hwall < pwall else "Pure mergesort"
    print(f"Faster by wall time: {faster}")
    
    print("\nGenerating bar graphs...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    algorithms = [f"Hybrid (S={S})", "Pure mergesort"]
    comparisons = [hcomparisons, pcomparisons]
    cpu_times = [hcpu, pcpu]
    comparisons_sci = [comp / 1e8 for comp in comparisons]  # Scale to 1e8 units
    bars1 = ax1.bar(algorithms, comparisons_sci, color=['#1f77b4', '#d62728'], alpha=0.8)
    ax1.set_title(f'Number of Comparisons (n={N:,})', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Comparisons', fontsize=12)
    ax1.set_ylim(0, max(comparisons_sci) * 1.1)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}'))
    ax1.tick_params(axis='y', labelsize=10)
    ax1.tick_params(axis='x', labelsize=10)
    
    for bar, value in zip(bars1, comparisons_sci):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'{value:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')  
   
    bars2 = ax2.bar(algorithms, cpu_times, color=['#1f77b4', '#d62728'], alpha=0.8)
    ax2.set_title(f'CPU Time (n={N:,})', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Seconds', fontsize=12)
    ax2.set_ylim(0, max(cpu_times) * 1.1)
     
    for bar, value in zip(bars2, cpu_times):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'{value:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    
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


partd()

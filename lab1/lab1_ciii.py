import time
import random

# Your hybrid sorting functions
def swap(A, x, y):
    A[x], A[y] = A[y], A[x]

def isort(A):
    comparison = 0
    for i in range(1, len(A)):
        for j in range(i, 0, -1):  
            comparison += 1
            if A[j] < A[j-1]:
                swap(A, j, j-1)
            else:
                break
    return comparison, A  

def merge(l, r):
    i = j = 0
    comparison = 0
    result = []
    while i < len(l) and j < len(r):
        comparison += 1
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return comparison, result

def hybrid_mergesort(A, S=10):
    if len(A) <= S:
        return isort(A)
    mid = len(A) // 2
    leftcomparison, left = hybrid_mergesort(A[:mid], S)
    rightcomparison, right = hybrid_mergesort(A[mid:], S)
    mergecomparison, merged = merge(left, right)
    totalc = leftcomparison + rightcomparison + mergecomparison
    return totalc, merged

def find_optimal_s():
    """Find optimal S using varying n values, prioritizing larger arrays"""
    
    # Test parameters - focusing on larger n values
    n_values = [5000, 10000, 20000, 50000]  # Higher values weighted more
    s_values = [4, 6, 8, 10, 12, 14, 16, 18, 20]
    trials = 3
    
    print("Finding Optimal S (focusing on larger arrays)")
    print(f"Array sizes: {n_values}")
    print(f"S candidates: {s_values}")
    
    s_scores = {}
    
    for S in s_values:
        total_score = 0
        
        for i, n in enumerate(n_values):
            weight = (i + 1) ** 2  
            
            times = []
            comparisons = []
            
            for _ in range(trials):
                arr = [random.randint(1, 10000) for _ in range(n)]
                
                start = time.perf_counter()
                comp_count, _ = hybrid_mergesort(arr, S)
                runtime = time.perf_counter() - start
                
                times.append(runtime)
                comparisons.append(comp_count)
            
            avg_time = sum(times) / len(times)
            avg_comparisons = sum(comparisons) / len(comparisons)
            
    
            time_score = 1 / avg_time  
            comp_score = 1 / avg_comparisons  
            combined = (0.7 * time_score + 0.3 * comp_score) * weight
            total_score += combined
        
        s_scores[S] = total_score
        print(f"S={S:2}: score={total_score:.1f}")
    
    # Find best S
    optimal_s = max(s_scores, key=s_scores.get)
    
    print(f"\nOptimal S: {optimal_s}")
    print(f"Best score: {s_scores[optimal_s]:.1f}")
    
    # Validate with largest array
    validate_optimal_s(optimal_s, max(n_values))
    
    return optimal_s

def validate_optimal_s(optimal_s, test_size):
    """Quick validation of optimal S"""
    print(f"\nValidation with n={test_size}:")
    
    results = []
    for S in [optimal_s-2, optimal_s, optimal_s+2]:  # Test neighbors
        if S < 2: continue
        
        arr = [random.randint(1, 10000) for _ in range(test_size)]
        
        start = time.perf_counter()
        comparisons, _ = hybrid_mergesort(arr, S)
        runtime = time.perf_counter() - start
        
        results.append((S, runtime, comparisons))
        print(f"S={S}: {runtime:.4f}s, {comparisons:,} comparisons")
    
    # Confirm optimal S is best
    best_s = min(results, key=lambda x: x[1])[0]  # Best time
    if best_s == optimal_s:
        print(f"S={optimal_s} is optimal")
    else:
        print(f" S={best_s} performed better in validation")

if __name__ == "__main__":
    random.seed(42)
    optimal_s = find_optimal_s()

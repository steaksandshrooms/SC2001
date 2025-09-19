# Hybrid Merge + Insertion Sort 

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
    # If array size is small enough, use insertion sort
    if len(A) <= S:
        
        return isort(A)

    mid = len(A) // 2
    leftcomparison, left = hybrid_mergesort(A[:mid], S)
    rightcomparison, right = hybrid_mergesort(A[mid:], S)
    mergecomparison, merged = merge(left, right)

    totalc = leftcomparison + rightcomparison + mergecomparison
    return totalc, merged


def pure_mergesort(A):
    # Base case
    if len(A) <= 1:
        return 0, A

    mid = len(A) // 2
    leftcomparison, left = pure_mergesort(A[:mid])
    rightcomparison, right = pure_mergesort(A[mid:])
    mergecomparison, merged = merge(left, right)

    totalc = leftcomparison + rightcomparison + mergecomparison
    return totalc, merged


# Example test
if __name__ == "__main__":
    A = [14, 40, 31, 28, 3, 15, 17, 51]

    # Hybrid version
    comparisons_hybrid, sortedA_hybrid = hybrid_mergesort(A, S=4)
    print("Hybrid Sorted:", sortedA_hybrid)
    print("Hybrid Comparisons:", comparisons_hybrid)

    # Pure mergesort version
    comparisons_pure, sortedA_pure = pure_mergesort(A)
    print("Pure Merge Sorted:", sortedA_pure)
    print("Pure Merge Comparisons:", comparisons_pure)

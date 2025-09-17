#merge sort
A = [14, 40, 31, 28, 3, 15, 17, 51]
B = [23, 23, 23, 23, 23, 23, 23, 23]
def merge(l,r):
    i = 0
    j = 0
    comparisoncount = 0
    result = []
    while i<len(l) and j<len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        comparisoncount += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result, comparisoncount

def mergesort(A):
    if len(A) <= 1:
        return A, 0
    mid = len(A)//2
    
    left, leftc = mergesort(A[:mid])
    right, rightc = mergesort(A[mid:])
    merged, mergec = merge(left, right)
    totalc = leftc + rightc + mergec
    return merged, totalc

print(mergesort(A))
print(mergesort(B))

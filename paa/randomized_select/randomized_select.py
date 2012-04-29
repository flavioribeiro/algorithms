def RANDOMIZED_PARTITION(A, p, r):
    x = A[r-1]
    i = p
    for j in range(p, r-1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r-1] = A[r-1], A[i]
    return i

def RANDOMIZED_SELECT(A, p, r, i):
    if p + 1 == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q, i)
    return RANDOMIZED_SELECT(A, q, r, i - k)



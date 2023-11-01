def fun(A):
    c = [0] * len(A[0])
    for i in range(len(c)): #liczenie srednich kolumn
        for j in range(len(A)):
            c[i] += A[j][i] 
        c[i] /= len(A)
    
    for i in range(len(c) - 1): #selection sort
        m = i
        for j in range(i + 1, len(c)):
            if c[m] > c[j]:
                m = j
        c[i], c[m] = c[m], c[i]
        
        for k in range(len(A)): #zamiana kolumn
            A[k][i], A[k][m] = A[k][m], A[k][i]

    return A

A = [[10, 100, 1] for _ in range(3)]
print(A)
print(fun(A))
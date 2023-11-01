import random
import math
import matplotlib.pyplot as plt

def macierz_startowa(n):
    return [[1 if i != j else 0 for i in range(n)] for j in range(n)]

def deg(A, i):
    d = 0
    n = len(A)
    for j in range(n):
        d += A[i][j]
    return d

def licznosc_stopni(A):
    D = [deg(A, i) for i in range(len(A))]
    dim = max(D) + 1

    K = [0] * dim
    for d in D:
        K[d] += 1
    
    return K


def nowe_grono(A, N, m):
    B = [[0] * N for _ in range(N)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = A[i][j]
    
    for i in range(len(A), N):
        losowo_wybrani = random.sample([j for j in range(i)], m)
        for wybrany in losowo_wybrani:
            B[i][wybrany] = 1
            B[wybrany][i] = 1

    return B
    
def p(k, m):
    if k < m:
        return 0
    else:
        return (math.e ** (1 - k/m)) / m

def srednie_bledy(T):
    N = 100
    m = 3
    n = 5
    A = macierz_startowa(n)
    v = [0] * N
    for i in range(T):
        suma = 0
        B = nowe_grono(A, N, m)
        k = licznosc_stopni(B)
        
        for j in range(N):
            if j < len(k):
                v[j] += k[j] - N * p(j, m)
            else:
                v[j] += 0 - N * p(j, m)

    for i in range(N):
        v[i] /= T

    return v

def main():
    random.seed(126)
    A = macierz_startowa(4)
    l = licznosc_stopni(A)
    for row in A:
        print(row)
    print(l)

    B = nowe_grono(A, 6, 2)
    for row in B:
        print(row)

    sb = srednie_bledy(1000)
    # 5 pierwszych elementów sb
    print(sb[:5])

    for i in range(len(sb)):
        plt.scatter(i, sb[i])
    plt.show()

if __name__ == '__main__':
    main()
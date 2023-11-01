import numpy
from PIL import Image
import math
import copy

def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size)==2 # skala szarosci, nie RGB
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

def pixels(A):
    max_v = float('-inf')
    min_v = float('inf')
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > max_v:
                max_v = A[i][j]
            if A[i][j] < min_v:
                min_v = A[i][j]
    return max_v, min_v

def rozjasnienie(A, b):
    B = copy.deepcopy(A)
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] += b
            if B[i][j] > 1:
                B[i][j] = 1
            if B[i][j] < 0:
                B[i][j] = 0
    return B

def negatyw(A):
    C = copy.deepcopy(A)
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = 1 - C[i][j]
    return C

def konwersja(A, p):
    D = copy.deepcopy(A)
    for i in range(len(D)):
        for j in range(len(D[0])):
            if D[i][j] > p:
                D[i][j] = 1
            else:
                D[i][j] = 0
    return D

def roz_kontr(A, t):
    E = copy.deepcopy(A)
    for i in range(len(E)):
        for j in range(len(E[0])):
            E[i][j] = f(E[i][j], t)

    return E

def f(c, t):
    e = math.e
    return 1/(1 + e ** (-t * (c * 0.5)))

def convolution(A, P):
    F = [[0] * len(A[0]) for _ in range(len(A))]
    k = len(P) // 2
    for i in range(len(F)):
        for j in range(len(F[0])):
            s1 = 0
            s2 = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    if i + u >= len(A) or j + v >= len(A[0]):
                        continue
                    else:
                        s1 += A[i + u][j + v] * P[u + k][v + k]
                s2 += s1
            F[i][j] = s2
    return F

def macierz_rozmycia(k):
    n = (2*k +1) * (2*k +1)
    return [[1/n] * (2*k + 1) for _ in range(2*k + 1)]

def main():
    A = png_read("skimage_astronaut.png")
    print(pixels(A))

    b = -0.5
    B = rozjasnienie(A, b)
    png_write(B, 'output_b.png')

    C = negatyw(A)
    png_write(C, 'output_c.png')

    p = 0.5
    D = konwersja(A, p)
    png_write(D, 'output_d.png')

    t = 2
    E = roz_kontr(A, t)
    png_write(E, 'output_e.png')

    k = 2
    P = macierz_rozmycia(k)
    F = convolution(A, P)
    png_write(F, 'output_F.png')

if __name__ == '__main__':
    main()
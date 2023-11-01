import csv
import math
import matplotlib.pyplot as plt

def read_csv(sciezka):
    A = []
    f = open(sciezka, "r") # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i]) # konwersja z str na float
        list.append(A, row) # == A.append(row)
    f.close()
    return A

def read_txt(sciezka):
    c = []
    with open(sciezka, 'r') as plik:
        for line in plik:
            c.append(int(line))
    return c

def check(A, c):
    for row in A:
        assert len(row) == 2
    assert len(A) == len(c)

    for element in c:
        assert element == 1 or element == 0

def distance(u, v):
    m = len(u)
    suma = 0
    for i in range(m):
        suma += (u[i] - v[i]) ** 2
    return math.sqrt(suma)

def nearest_neighbour_class(A, c, z):
    min_dist = float('inf')
    n = len(A)
    for i in range(n):
        dist = distance(A[i], z)
        if dist < min_dist:
            min_dist = dist
            i_min = i
    
    return c[i_min]

def knn(A, c, Z):
    l = []
    for z in Z:
        l.append(nearest_neighbour_class(A, c, z))
    return l

def gen_x_y(A, N):
    a0 = float('inf')
    a1 = float('-inf')
    b0 = float('inf')
    b1 = float('-inf')
    for i in range(len(A)):
        if A[i][0] > a1:
            a1 = A[i][0]
        if A[i][0] < a0:
            a0 = A[i][0]
    for i in range(len(A)):
        if A[i][1] > b1:
            b1 = A[i][1]
        if A[i][1] < b0:
            b0 = A[i][1]
    x = []
    r = (a1 - a0) / (N - 1)
    for i in range(N):
        x.append(a0 + r * i)

    y = []
    t = (b1 - b0) / (N - 1)
    for i in range(N):
        y.append(b0 + t * i)

    return x, y

def gen_Z(A, N):
    x, y = gen_x_y(A, N)
    Z = [[None] * 2 for _ in range(N * N)]
    p = 0
    for i in range(N):
        for j in range(N):
            Z[p][0], Z[p][1] = x[i], y[j]
            p += 1
    return Z

def wykres(A, Z, c, c_z):
    fig = plt.figure()
    for i in range(len(A)):
        u = A[i][0]
        v = A[i][1]
        plt.scatter(u, v, c="b" if c[i] else "r") # dla list u i v (o takim samym rozmiarze)
            # punkty o wspolrzednych (u[i], v[i]) beda oznaczone
            # punktami o kolorach wskazanych przez kolejne elementy
            # listy ["b", "r", ...]
    for i in range(len(Z)):
        w = Z[i][0]
        q = Z[i][1]
        plt.scatter(w, q, alpha = 0.2, marker=".", c="b" if c_z[i] else "r") # dla list w i q (o takim samym      rozmiarze)
            # punkty o wspolrzednych (w[i], q[i]) beda oznaczone
            # punktami o ksztalcie . i kolorach wskazanych przez kolejne elementy listy
    fig.savefig("output.png", dpi=90)

def klasyfikator(c_t, c_t_z):
    TN = 0
    FP = 0
    FN = 0
    TP = 0
    
    for i in range(len(c_t)):
        if c_t[i] == 0 and c_t_z[i] == 0:
            TN += 1
        elif c_t[i] == 0 and c_t_z[i] == 1:
            FP += 1
        elif c_t[i] == 1 and c_t_z[i] == 0:
            FN += 1
        elif c_t[i] == 1 and c_t_z[i] == 1:
            TP += 1
    
    return TN, FN, TP, FP

def output(TN, FN, TP, FP):
    d = (TP + TN)/ (TN + FN + TP + FP)
    p = TP/(TP + FP)
    c = TP/(TP + FN)
    f1 = 2*TP/(2*TP + FP + FN)
    
    with open('output.txt', 'w') as plik:
        print(f"  |{'0':^10}|{'1':^10}",file=plik)
        print("-" * 25, file=plik)
        print(f"0 |{TN:^10}|{FP:^10}", file=plik)
        print(f"1 |{FN:^10}|{TP:^10}", file=plik, end='\n\n')
        print(round(d, 2), round(p, 2), round(c, 2), round(f1, 2), sep='\n', file=plik)

def main(): 
    A = read_csv('train_wine.csv')
    c = read_txt('train_class.txt')
    check(A, c)
    
    N = 100
    Z = gen_Z(A, N)
    c_z = knn(A, c, Z)
    #wykres(A, Z, c, c_z)

    test = read_csv('test_wine.csv')
    c_t = read_txt('test_class.txt')
    c_t_z = knn(A, c, test)
    
    TN, FN, TP, FP = klasyfikator(c_t, c_t_z)
    output(TN, FN, TP, FP)


if __name__ == '__main__':
    main()
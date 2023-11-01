import random
import math

def wylosuj_klocek(n, m):
    klocek = [[False] * m for _ in range(n)]
    i = random.randint(0, n - 1)
    j = random.randint(0, m - 1)
    klocek[i][j] = True

    for r in range(n):
        for c in range(m):
            if r != i or c != j:
                d = math.sqrt((r - i)**2 + (c - j)**2)
                klocek[r][c] = random.choices([True, False], [1/(d+1), d/(d + 1)], k=1)[0]
    return klocek

def spusc_klocek(plansza, klocek):
    n = len(plansza)
    k = len(klocek)
    for r in range(len(klocek)):
        for c in range(len(klocek[0])):
            if klocek[r][c] and not plansza[r][c]:
                plansza[r][c] = True

def wypisz_macierz(M):
    for j in range(len(M[0]) + 2):
        print("-", end="")

    print()

    for i in range(len(M) - 1, -1, -1):
        print("|", end="")
        for j in range(len(M[i])):
            if M[i][j]:
                print("#", end="")
            else:
                print(" ", end="")
        print("|")

    for j in range(len(M[0]) + 2):
        print("-", end="")
    print()

def main():
    n = int(input("Podaj wysokość planszy: "))
    m = int(input("Podaj szerokość planszy: "))
    k = int(input("Podaj wysokość klocka: "))
    if k > n:
        raise ValueError("Błędne dane")

    plansza = [[False] * m for _ in range(n)]
    #w_planszy = True
    #while w_planszy:
    klocek = wylosuj_klocek(k, m)
    w_planszy = spusc_klocek(plansza, klocek)
    print('Klocek:')
    wypisz_macierz(klocek)
    print('Stan po zrzuceniu klocka:')
    wypisz_macierz(plansza)
    

if __name__ == "__main__":
    main()
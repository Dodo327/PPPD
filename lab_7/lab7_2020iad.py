import random
import math
import copy

def wygeneruj_prosta_sciezke(n):
    lista = [None] * n
    for i in range(0, n):
        lista[i] = i

    return lista

def wygeneruj_miasta_A(n, min_x=-10, max_x=10, min_y=-10, max_y=10):
    lista_x = [None] * n
    lista_y = [None] * n
    
    for i in range(n):
        lista_x[i] = random.uniform(min_x, max_x)
        lista_y[i] = random.uniform(min_y, max_y)
    
    return lista_x, lista_y

def oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka):
    droga = 0
    for i in range(len(sciezka)):
        m1 = sciezka[i]
        if i + 1 > len(sciezka) - 1:
            m2 = sciezka[0]
        else:
            m2 = sciezka[i + 1]
        droga += math.sqrt((miasta_x[m1] - miasta_x[m2]) ** 2 + (miasta_y[m1] - miasta_y[m2]) ** 2)
    
    return droga

def mutuj_A(sciezka, k=3):
    zmutowana = copy.deepcopy(sciezka)
    
    indeksy = random.sample(sciezka, k)
    z = zmutowana[indeksy[0]]
    for i in range(k):
        if i + 1 > k - 1:
            zmutowana[indeksy[i]] = z
        else:
            zmutowana[indeksy[i]] = zmutowana[indeksy[i + 1]]
    
    return zmutowana 

def krzyzuj_A(sciezka1, sciezka2):
    indeks = random.randint(1, len(sciezka1) - 2)
    dziecko = [None] * len(sciezka1)
    for i in range(len(dziecko)):
        if i < indeks:
            dziecko[i] = sciezka1[i]
        else:
            for j in range(len(dziecko)):
                if dziecko[j] is None:
                    break
                if sciezka2[i - indeks] == dziecko[j]:
                    indeks -= 1
            dziecko[i] = sciezka2[i - indeks]
       
    return dziecko

def znajdz_rozwiazanie_optymalne_A(n, miasta_x, miasta_y):
    c = [None] * n

    for i in range(len(c)):
        c[i] = 0
    
    A = wygeneruj_prosta_sciezke(n)
    oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, A)

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                A[0], A[i] = A[i], A[0]
            else:
                A[c[i]], A[i] = A[i], A[c[i]]
            
            oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, A)

            c[i] += 1

            i = 0
        else:
            c[i] = 0
            i += 1
    
    return oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, A), A


def main_A():
    random.seed(123)
    n = 7
    min_x, max_x, min_y, max_y = -5, 4, -4, 5
    # grupa A
    # etap 1
    print("0. Generujemy miasta")
    miasta_x, miasta_y = wygeneruj_miasta_A(n, min_x, max_x, min_y, max_y)
    print(miasta_x)
    print(miasta_y)

    print("\n\n1. Szukamy prostą mutacją")
    sciezka = wygeneruj_prosta_sciezke(n)
    print(f"Prosta sciezka: {sciezka}")
    best_sciezka = sciezka
    best_wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    print(f"Dla prostej ścieżki długość ścieżki to: {best_wartosc}")

    print(f"mutuj_A([0,1,2,3,4,5,6], 3) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 3)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 4) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 4)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 5) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 5)}")
    
    
    sciezka100 = best_sciezka
    for i in range(100):
        sciezka100 = mutuj_A(sciezka100)
        if oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka100) < best_wartosc:
            best_sciezka = sciezka100
            best_wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka100)
    
    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")

    print("\n\n2. Szukamy przez krzyzowanie")

    sciezka1 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka2)

    for i in range(1000):
        dziecko = krzyzuj_A(sciezka1, sciezka2)
        wartosc_d = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, dziecko)

        if wartosc_d < wartosc2:
            wartosc2 = wartosc_d
            sciezka2 = dziecko
        
        if wartosc2 < wartosc1:
            wartosc1, wartosc2 = wartosc2, wartosc1
            sciezka1, sciezka2 = sciezka2, sciezka1

    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")

    # etap 5:

    optymalne = znajdz_rozwiazanie_optymalne_A(n, miasta_x, miasta_y)
    print(f"\n\n3. Optymalny wynik to {optymalne}")


if __name__ == "__main__":
    main_A()

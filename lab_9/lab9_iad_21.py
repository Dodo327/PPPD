import csv
import copy


def wczytaj_dane(sciezka):
    M = []
    f = open(sciezka)
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = int(row[i]) # konwersja z str na int
        list.append(M, row) # == A.append(row)
    f.close()
    return M

def wypisz(dane):
    print(end='   ')
    for i in range(len(dane[0])):
        print(i, end=' ')
    
    print()
    for i in range(len(dane)):
        print(f'{i}:', end=' ')
        for j in range(len(dane[0])):
            print(dane[i][j], end=' ')
        print()

def bezpieczne(row, lista):
    for alergen in lista:
        if row[alergen]:
            return False
    return True

def szukaj_bezpiecznych_dan(dane, lista):
    return [i for i in range(len(dane)) if bezpieczne(dane[i], lista)]

def dodaj_nowe_danie(dane, lista):
    n = len(dane) + 1
    m = len(dane[0])
    nowe_dane = [[None] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i < len(dane):
                nowe_dane[i][j] = dane[i][j]
            else:
                if j in lista:
                    nowe_dane[i][j] = 1
                else:
                    nowe_dane[i][j] = 0
    return nowe_dane

def dobry(row, k):
    return sum(row) < k

def usun_najgorsze(dane, k):
    return [row.copy() for row in dane if dobry(row, k)]

def zapisz_informacje(dane, sciezka):
    max_dane = max([sum(row) for row in dane])
    liczba_alergenow = [0] * (max_dane + 1)
    for row in dane:
        liczba_alergenow[sum(row)] += 1
        
    with open(sciezka, 'w') as plik:
        print(f'liczba dan: {len(dane)}', file=plik)
        print(f'liczba uwzglednionych alergenow: {len(dane[0])}', file=plik)
        print(f'maksymalna liczba alergenow: {max_dane}', file=plik)
        for i in range(len(liczba_alergenow)):
            print(f'liczba dan z {i} alergenow: {liczba_alergenow[i]}', file=plik)

        
def main():
    dane = wczytaj_dane('alerg.csv')
    wypisz(dane)
    
    print("dania bez 0, 5, 10")
    print(szukaj_bezpiecznych_dan(dane, [0, 5, 10]))

    print("dodane nowe danie z alergenami 1, 2, 3, 8")
    dane = dodaj_nowe_danie(dane, [1, 2, 3, 8])
    wypisz(dane)

    print("dania po usunieciu tych z co najmniej 5 alergenami")
    dane = usun_najgorsze(dane, 5)
    wypisz(dane)

    zapisz_informacje(dane, "zapis.txt")

if __name__ == '__main__':
    main()
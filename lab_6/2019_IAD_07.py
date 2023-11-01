def podaj():
    rozmiar = int(input("Podaj najwiekszy element zbioru: ")) + 1
    lista = [None] * rozmiar

    for i in range(0, rozmiar):
        x = int(input(f"Podaj ilość {i}: ")) 
        if x < 0 or (i == rozmiar and x == 0):
            raise ValueError("Błędne dane!")
        
        lista[i] = x
    return lista

def wypisz(lista):
    rozmiar = 0
    for i in range(0, len(lista)):
        rozmiar += lista[i]
    
    multizbior = [None] * rozmiar
    x = 0
    for i in range(0, len(lista)):
        for j in range(x, x + lista[i]):
            if lista[i] != 0:
                multizbior[j] = i
        x += lista[i]
    print(multizbior)

def dodaj(zbior, element):
    if element in range (0, len(zbior)):
        zbior[element] += 1
        return zbior
    else:
        zbior_nowy = [None] * (element + 1)
        for i in range(0, len(zbior_nowy)):
            if i < len(zbior):
                zbior_nowy[i] = zbior[i]
            elif i != element:
                zbior_nowy[i] = 0
            elif i == element:
                zbior_nowy = element
        
        return zbior_nowy

def przeciecie(zbior_A, zbior_B):
    zbior_przeciecie = [None] * min(len(zbior_A), len(zbior_B))

    for i in range(0, len(zbior_przeciecie)):
        zbior_przeciecie[i] = min(zbior_A[i], zbior_B[i])

    return zbior_przeciecie

def roznica(zbior_A, zbior_B):
    zbior_roznica = [None] * max(len(zbior_A), len(zbior_B))
    for i in range(0, len(zbior_roznica)):
        if i >= len(zbior_A):
            zbior_roznica[i] = zbior_B[i]
        elif i >= len(zbior_B):
            zbior_roznica[i] = zbior_A[i]
        else:
            zbior_roznica[i] = abs(zbior_A[i] - zbior_B[i])

    return zbior_roznica


def main():
    print("Zbior A:")
    zbior_A = podaj()
    print("Podany zbior to" )
    wypisz(zbior_A)
    element = int(input("Podaj nowy element zbioru A: "))
    zbior_A = dodaj(zbior_A, element)
    print("Zbiór A po dodaniu elementu:")
    wypisz(zbior_A)

    print("Zbior B:")
    zbior_B = podaj()
    print("Podany zbior to" )
    wypisz(zbior_B)

    zbior_przeciecie = przeciecie(zbior_A, zbior_B)
    print("Przecięcie zbiorów:")
    wypisz(zbior_przeciecie)

    zbior_roznica = roznica(zbior_A, zbior_B)
    print("Różnica tych zbiorów: ")
    wypisz(zbior_roznica)

if __name__ == "__main__":
    main()
import random

def losuj_litery(dlugosc):
    lista = [None] * dlugosc
    for i in range(0, dlugosc):
        lista[i] = chr(random.randint(97, 122))

    return lista

def polacz_z_zawijaniem(pierwsza, druga):
    n = 2 * max(len(pierwsza), len(druga))
    polaczona = [None] * n
    for i in range(0, n):
        if len(pierwsza) >= len(druga):
            if i < n / 2:
                polaczona[i] = pierwsza[i]
            else:
                polaczona[i] = druga[(i - n / 2) % len(druga)]
        
        elif len(druga) > len(pierwsza):
            if i < n / 2:
                polaczona[i] = pierwsza[i % len(pierwsza)]
            else:
                polaczona[i] = druga[int(i - n / 2)]
    
    return polaczona

def odwroc(lista, poczatek, koniec):
    for i in range(koniec - poczatek - 1):
        lista[poczatek + i], lista[koniec - i] = lista[koniec - i], lista[poczatek + i]

def przesun_w_lewo(lista, x):
    i = 0
    j = 0
    k = lista[0]
    
    while j < len(lista):
        if (i + x) % len(lista) == 0:
            lista[i] = k
        else:
            lista[i] = lista[(i + x) % len(lista)]
        i = (i + x) % len(lista)
        j += 1
    
    return lista

def mod_26(tab):
    k = tab[0]
    for i in range(len(tab)):
        if i - 1 < 0:
            a = 0
        else:
            a = ord(k)
        
        b = ord(tab[i])

        if i + 1 > len(tab) - 1:
            c = 0
        else:
            c = ord(tab[i + 1])

        k = tab[i]
        tab[i] = chr((a + b + c) % 26 + 97)
    return tab

def main():
    random.seed(2014)
    '''dlugosc = int(input(("Podaj długość bazową: ")))
    if not 5 <= dlugosc <= 15:
        raise ValueError("Błędne dane")'''
    
    lista1 = losuj_litery(7)
    print(lista1)
    lista2 = losuj_litery(15)
    print(lista2)

    polaczona = polacz_z_zawijaniem(lista1, lista2)
    print(polaczona)

    odwroc(lista2, 3, 7)
    print(lista2)

    przesun_w_lewo(lista1, 3)
    print(lista1)

    m = ['a', 'b', 'c', 'd']
    mod_26(m)
    print(m)

if __name__ == "__main__":
    main()
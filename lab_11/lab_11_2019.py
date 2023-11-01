def wczytaj(sciezka):
    lista = []
    with open(sciezka, 'r') as file:
        for line in file:
            line = int(line)
            if line >= 0:
                lista.append(line)
    return lista

def sprawdz_poprawnosc(lista):
    if len(lista) == 0:
        return False
    
    for i in lista:
        if i < 0 or type(i) != int:
            return False
    return True

def podziel(lista):
    if not sprawdz_poprawnosc(lista):
        raise Exception("Zła lista")
    t = [[]]
    i0 = float('-inf')
    j = 0
    for i in lista:
        if i <= i0:
            t.append([])
            j += 1
        t[j].append(i)
        i0 = i
    return t

def wypisz(lista):
    for i in range(len(lista)):
        print(f'x[{i}]:', end='\t')
        for j in lista[i]:
            print(j, end='\t')
        print()

def zlacz_posortowane(lista):
    pass

def main():
    lista = wczytaj('dane.txt')
    z = podziel(lista)
    wypisz(z)

if __name__ == '__main__':
    main()
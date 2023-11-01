import csv

def wczytaj_csv(nazwa_pliku):
    data = []
    data = []
    with open(nazwa_pliku) as f:
        for row in csv.reader(f):
            data.append([float(row[i]) if i == 0 else row[i]
                                          for i in range(len(row))])
    return data

def sprawdz_poprawnosc(y):
    if len(y) == 0:
        return False
    
    for i in range(len(y)):
        if len(y[i]) != 3:
            return False
        if type(y[i][0]) != float:
            return False
        if type(y[i][1]) != str:
            return False
        if type(y[i][2]) != str:
            return False
    return True

def kategorie(y, i):
    if type(y[0][i]) != str:
        raise Exception('Zła kolumna.')
    kat = []
    for j in range(len(y)):
        if y[j][i] not in kat:
            kat.append(y[j][i])
    return kat

def grupuj(lista, by):
    kat = kategorie(lista, by)
    k = len(kat)
    gr = [[] for _ in range(k)]
    
    for i in range(len(lista)):
        for j in range(k):
            if lista[i][by] == kat[j]:
                gr[j].append(lista[i])
    
    gr.append(kat)
    return gr

def policz(y_grupy, f, i):
    kat = y_grupy[len(y_grupy) - 1]
    k = len(kat)
    i_grupy = [[] for _ in range(k)]
    licz = [kat, [None for _ in range(k)]]

    for j in range(k):
        for el in y_grupy[j]:
            i_grupy[j].append(el[i])

        licz[1][j] = f(i_grupy[j])
    return licz

def main():
    tips = wczytaj_csv('2021-MAT-11_tips.csv')
    
    print(sprawdz_poprawnosc(tips))
    print(kategorie(tips, 2))
    
    grupy = grupuj(tips, 2)
    
    print(policz(grupy, len, 0))
    print(policz(grupy, lambda x: sum(x)/len(x), 0))
    
    

if __name__ == '__main__':
    main()
import math
import matplotlib.pyplot as plt
import numpy
from PIL import Image

def png_write(img):
    img = Image.fromarray((numpy.array(img) * 255).astype(numpy.int8), 'L')
    img.save("output.png")

def trzeci_punkt_trojkata_rownobocznego(p1, p2):
    odleglosc = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    srodek = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    kat = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    wynik_x = srodek[0] - odleglosc * 3 ** 0.5 / 2 * math.sin(kat)
    wynik_y = srodek[1] + odleglosc * 3 ** 0.5 / 2 * math.cos(kat)
    return [wynik_x, wynik_y]

def narysuj_wielokat(lista_wierzcholkow):
    x = []
    y = []
    for p in lista_wierzcholkow:
        x.append(p[0])
        y.append(p[1])
    x.append(lista_wierzcholkow[0][0])
    y.append(lista_wierzcholkow[0][1])
    
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()

def kolejna_iteracja(lista):
    platek = []
    for i in range(len(lista)):
        p0 = lista[i]
        if i == len(lista) - 1:
            p4 = lista[0]
        else:
            p4 = lista[i + 1]
       
        d = [p4[0] - p0[0], p4[1] - p0[1]]
        p1 = [p0[0] + d[0] / 3, p0[1] + d[1] / 3]
        p2 = [p0[0] + 2 * d[0] / 3, p0[1] + 2 * d[1] / 3]
        p3 = trzeci_punkt_trojkata_rownobocznego(p1, p2)
        platek.append(p0)
        platek.append(p1)
        platek.append(p3)
        platek.append(p2)
    return platek

def platek_sniegu_Kocha(d):
    p1 = [0, 0]
    p3 = [d, 0]
    p2 = trzeci_punkt_trojkata_rownobocznego(p1, p3)
    lista = [p1, p2, p3]
    
    n = 0
    while n < 10:
        n += 1
        lista = kolejna_iteracja(lista)
    narysuj_wielokat(lista)
    wypelniony_wielokat(lista)

def podpodzial(lista):
    podzial = []
    for i in range(len(lista)):
        p1 = lista[i]
        podzial.append(p1)
        if i == len(lista) - 1:
            p2 = lista[0]
        else:
            p2 = lista[i + 1]

        odleglosc = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        n = math.ceil(odleglosc)
        if odleglosc > 1:
            for i in range(n):
                p = [(p1[0] * i + (n - i) * p2[0])/n, (p1[1] * i + (n - i) * p2[1])/n]
                podzial.append(p)

def wypelniony_wielokat(lista):
    podpodzial(lista)
    x_max = float('-inf')
    x_min = float('inf')
    y_max = float('-inf')
    y_min = float('inf')
    for i in range(len(lista)):
        lista[i][0] = int(lista[i][0])
        lista[i][1] = int(lista[i][1])
        if lista[i][0] > x_max:
            x_max = lista[i][0]
        if lista[i][0] < x_min:
            x_min = lista[i][0]
        if lista[i][1] > y_max:
            y_max = lista[i][1]
        if lista[i][1] < y_min:
            y_min = lista[i][1]
    print(x_max, x_min, y_max, y_min)
    obraz = [[0 for _ in range(abs(x_max - x_min) + 1)] for _ in range(abs(y_max - y_min) + 1)]

    for i in range(len(lista)):
        m = lista[i][0]
        n = lista[i][1]
        if x_min != 0:
            m -= x_min
        if y_min != 0:
            n -= y_min
        
        obraz[n][m] = 1

    p_wew = []
    png_write(obraz)

def main():
    platek_sniegu_Kocha(200)
    pass

if __name__ == '__main__':
    main()
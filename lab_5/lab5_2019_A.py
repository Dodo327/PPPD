import random

def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False

def wypisz_prostokat(x_min, x_max, y_min, y_max):
    print(f"[{x_min}, {x_max}] x [{y_min}, {y_max}]")

def najmniejszy_plot(x_min, x_max, y_min, y_max):
    najmniejszy_x = None
    najwiekszy_x = None
    najmniejszy_y = None
    najwiekszy_y = None
    if x_min >= x_max or y_min >= y_max:
        return 0, 0, 0, 0
    
    jest_drzewo = False
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if drzewo(i, j):
                jest_drzewo = True
                if najmniejszy_x == None or najmniejszy_x > i:
                    najmniejszy_x = i
                if najmniejszy_y == None or najmniejszy_y > j:
                    najmniejszy_y = j
                if najwiekszy_x == None or najwiekszy_x < i:
                    najwiekszy_x = i
                if najwiekszy_y == None or najwiekszy_y < j:
                    najwiekszy_y = j
                
    if not jest_drzewo:
        return 0, 0, 0, 0
    return najmniejszy_x, najwiekszy_x, najmniejszy_y, najwiekszy_y

def zapisz_do_pliku(sciezka, x_min, x_max, y_min, y_max):
    with open(sciezka, 'w') as plik:
        for i in range(y_max, y_min - 1, -1):
            print(i, end='\t', file= plik)
            for j in range(x_min, x_max + 1):
                if drzewo(j, i):
                    print('D', end='', file= plik)
                elif not drzewo(j, i):
                    print('.', end='', file = plik)
            print('', file = plik)
        print('y/x', end=' ', file = plik)
        for z in range(x_min, x_max + 1):
            print(z, end='', file = plik)

def obwod_prostokata(x_min, x_max, y_min, y_max):
    return 2 * ((x_max - x_min) + (y_max - y_min))

def najlepszy_podzial(x_min, x_max, y_min, y_max):
    najlepszy_x = None
    a, b, c, d = najmniejszy_plot(x_min, x_max, y_min, y_max)
    najlepszy_obwod = obwod_prostokata(a, b, c, d)
    
    for i in range(x_min, x_max + 1):
        a1, b1, c1, d1 = najmniejszy_plot(x_min, i, y_min, y_max)   
        a2, b2, c2, d2 = najmniejszy_plot(i + 1, x_max, y_min, y_max)
     
        nowy_obwod = obwod_prostokata(a1, b1, c1, d1) + obwod_prostokata(a2, b2, c2, d2)

        if nowy_obwod < najlepszy_obwod:
            najlepszy_obwod = nowy_obwod
            najlepszy_x = i
    
    return najlepszy_x

def drzewo2(x, y):
    if x > 10 or x < -10:
        return False
    if y > 10 or y < -10:
        return False

    if 0 <= x <= 10 and -10 <= y <= 10:
        szansa = random.choices([0, 1], [0.5, 0.5], k = 1)
        if szansa == 0:
            return False

    if -10 <= x <= -1 and -10 <= y <= 10:
        szansa = random.choices([0, 1], [0.1, 0.9], k = 1)
        if szansa == 0:
            return False        


def main():
    print("Podaj wymiary sadu w kolejnosci xmin, xmax, ymin, ymax")
    x_min = int(input())
    x_max = int(input())
    y_min = int(input())
    y_max = int(input())

    print("Podany prostokąt to:")
    wypisz_prostokat(x_min, x_max, y_min, y_max)

    a, b, c, d = najmniejszy_plot(x_min, x_max, y_min, y_max)
    print("Najmniejszy płot zawierający wszystkie drzewka:")
    wypisz_prostokat(a, b, c, d)

    print("Obwód sadu:" ,obwod_prostokata(x_min, x_max, y_min, y_max))

    print("Obwód plotu:", obwod_prostokata(a, b, c, d))

    x_naj = najlepszy_podzial(x_min, x_max, y_min, y_max)
    print("Najlepszy podział to", x_naj)

    sciezka = input("Podaj nazwe pliku do zapisu: ")
    zapisz_do_pliku(sciezka, x_min, x_max, y_min, y_max)


if __name__ == "__main__":
    main()
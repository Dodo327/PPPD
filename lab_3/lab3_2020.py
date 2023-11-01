import math
def main():
    x = int(input("Podaj liczbe całkowita wiekszą niż 1: "))
    dzielniki_p = {}
    najwięcej = 0
    ilość = 0
    iloczyn = 1
    
    if x <= 1:
        raise Exception("Liczba miała być wieksza niż 1!")

    for i in range(2, x):
        pierwsze = True
        y = x
        if x % i == 0:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    pierwsze = False
                    break
            
            if pierwsze:
                dzielniki_p[i] = 0
                while y % i == 0:
                    y /= i
                    dzielniki_p[i] += 1

    print(f"Dzielniki pierwsze liczby {x} to: ")
    for keys in dzielniki_p:
        print(keys)
        iloczyn *= keys
        
    for keys, values in dzielniki_p.items():
        if values > ilość:
            najwięcej = keys
            ilość = values
    print(f"W rozkladzie {x} na czynniki pierwsze najczęściej pojawia się {najwięcej}, występuje {dzielniki_p[najwięcej]} razy.")
    print(f"Jeżeli w rozkładzie {x} na czynniki pierwsze pominiemy krotności, otrzymamy liczbę {iloczyn}.")

if __name__ == "__main__":
    main()
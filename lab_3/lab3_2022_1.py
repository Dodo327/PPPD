def main():    
    n = int(input("Podaj liczbę tygodni: "))
    k = int(input("Podaj liczbę worków do kupienia: "))
    k_1 = k
    k_2 = k
    koszt_1 = 0
    koszt_2 = 0
    tydzień = 0
    cena_0 = 0
    cena_1 = 0
    cena_2 = 0
    cena_3 = 0

    if n <= 5 or k <= 0:
        raise ValueError("Błędne dane.")

    while tydzień < n:
        tydzień += 1
        cena_1, cena_2, cena_3 = cena_0, cena_1, cena_2
        cena_0 = int(input(f"Podaj cenę węgla w tygodniu {tydzień}: "))
        
        if tydzień == n:
            if k_1 > 0:
                koszt_1 += cena_0 * k_1
                print(f"Pierwszy gospodarz kupił {k_1} worki węgla.")
            if k_2 > 0:
                koszt_2 += cena_0 * k_2
                print(f"Drugi gospodarz kupił {k_2} worki węgla.")
            continue
        
        if cena_0 < cena_1 < cena_2 < cena_3 and k_1 > 0:
            koszt_1 += cena_0 * (k / 4)
            k_1 -= k / 4
            print(f"Pierwszy gospodarz kupił {k / 4} worki węgla.")

        if cena_0 < cena_1 and k_2 > 0:
            if k_2 == 1:
                k_2 -= 1
                koszt_2 += cena_0
                print("Drugi gospodarz kupił 1 worek węgla.")
            else:
                k_2 -= 2
                koszt_2 += cena_0 * 2
                print("Drugi gospodarz kupił 2 worki węgla.")

    print(f"Pierwszy gospodarz zapłacił {koszt_1} zł.")
    print(f"Drugi gospodarz zapłacił {koszt_2} zł")

    if koszt_1 > koszt_2:
        print(f"Drugi gospodarz zapłacił  o {koszt_1 - koszt_2} zł mniej.")
    elif koszt_2 > koszt_1:
        print(f"Pierwszy gospodarz zapłacił  o {koszt_2 - koszt_1} zł mniej.")
    else:
        print("Obaj gospodarze zapłacili tyle samo.")

if __name__ == "__main__":
    main()
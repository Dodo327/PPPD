"""
Funkcja main() jest funkcją główną naszego programu.
Będziemy ją uruchamiac jeżeli nasz skrypt zostanie uruchomiony bezpośrednio (nie przez import)
"""

def main():

    a = 5       # int - liczba całkowita
    b = 6.8     # float - liczba zmiennopozycyjna (rzeczywista)
    c = True    # bool - zmienna logiczna, przyjmuje wartości True (prawda) albo False (fałsz) - wielkość liter ma znaczenie
    s = "napis" # str - napis

    a = 3.6     # teraz a jest typu float
    a = "8.7"   # teraz a jest napisem

    # wypisywanie
    print("Zmienna a ma wartość: ", a)
    print("Zmienna b ma wartość: ", b)
    print("Zmienna b ma wartość: " + str(b))  # str(b) konwertuje swój parametr na napis
                                            # analogiczne funkcje: int(), float(), bool()
    print(f"Zmienna c ma wartość: {c}, a s ma wartość: {s}")

    # *ciekawostka
    print("Zmienna", "c", "ma", "wartość", c, ".", sep=" ", end="\n")  # wypisane tak samo jak wyżej
    print("Zmienna", "c", "ma", "wartość", c, ".", sep="_", end="*")
    print("Zostaliśmy w tej samej linii...")

    # wczytywanie
    # wynik funkcji input jest typu str, jeżeli chcemy mieć zmienną innego typu musimy dokonać konwersji
    print("Podaj pierwsze słowo")
    s1 = input()
    print(f"Podales: {s1}")

    s2 = input("Podaj drugie słowo")    # możemy podać wyświetlany tekst jako parametr funkcji input
    print(f"Podales: {s2}")

    a = int(input("A teraz podaj liczbę"))
    print(f"Podales: {a}")

    # operatory arytmetyczne
    print(f"4.5 + 2 = {4.5 + 2}")    # dodawanie
    print(f"4.5 - 2 = {4.5 - 2}")    # odejmowanie
    print(f"4.5 * 2 = {4.5 * 2}")    # mnożenie
    print(f"4.5 / 2 = {4.5 / 2}")    # dzielenie
    print(f"4.5 // 2 = {4.5 // 2}")  # dzielenie całkowite
    print(f"4.5 // 2.1 = {4.5 // 2.1}")  # dzielenie całkowite
    print(f"4.5 % 2 = {4.5 % 2}")    # reszta z dzielenia
    print(f"4.75 % 2.25 = {4.75 % 2.25}")  # reszta z dzielenia
    print(f"-3 % 8 = {-3 % 8}")  # reszta z dzielenia
    print(f"3 % -8 = {3 % -8}")  # reszta z dzielenia
    print(f"-3 % -8 = {-3 % -8}")  # reszta z dzielenia
    print(f"4.5 ** 2 = {4.5 ** 2}")  # potęgowanie

    a = 5
    print(f"a ma wartość {a}")
    a += 1
    print(f"zwiększamy ją o 1: a += 1 == {a}") #analogicznie dla innych operatorów arytmetycznych

    # operatory porównania:
    # < > <= >= == !=
    print("1 < 10:", 1 < 10)
    print("5.0 == \"5.0\":",5.0 == "5.0")
    print("1 != 1.0:", 1 != 1.0)
    print("1 == 1.0:", 1 == 1.0)
    print("1.5 >= True:", 1.5 >= True)
    print("1 == True:", 1 == True)
    print("0 == False:", 0 == False)

    # porownywanie napisow - porzadek leksykograficzny
    print("\"ala\" < \"basia\":", "ala" < "basia")
    print("\"ala\" < \"abc\":", "ala" < "abc")
    print("\"ala\" < \"123\":", "ala" < "123")

    # operatory logiczne
    # or - lub
    # and - i
    # not - zaprzeczenie

    print("1 < 2 and 2 > 3 :", 1 < 2 and 2 > 3)
    print("not 1 < 2 and 2 < 3 :", not 1 < 2 and 2 < 3)
    print("not 1 < 2 or 2 < 3 :", not 1 < 2 or 2 < 3)

    # instrukcje warunkowe
    s = input("Wpisz True albo False")

    if s == "True":
        print("Prawda")

    # jeszcze raz, trochę inaczej
    s = input("True czy False?")
    if s == "True":
        print("Prawda")
    else:
        print("Fałsz")

    # jeszcze raz, jeszcze inaczej
    s = input("True czy False?")

    if s == "True":
        print("Prawda")
    elif s == "False":
        print("Fałsz")
    else:
        print("Błędne dane!")

    # jeszcze raz, tym razem przy błędnych danych rzucamy wyjątek
    s = input("True czy False?")

    if s == "True":
        print("Prawda")
    elif s == "False":
        print("Fałsz")
    else:
        raise Exception("Błędne dane!")

    import math  # import modułu z funkcjami matematycznymi
    print (math.sqrt(4))  # pierwiastek kwadratowy
    print (math.pi)  # pi
    print (math.floor(4.28))  # podłoga
    print (math.ceil(4.28))  # sufit
    print (math.fabs(-1.11))  # wartość bezwzględna


if __name__ == "__main__":      # jeżeli nasz skrypt został uruchomiony bezpośrednio to wywołujemy funkcję main()
    main()
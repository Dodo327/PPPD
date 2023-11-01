import random

def ruch():
    print("Co chcesz zrobić?")
    print("1 - skok")
    print("2 - mega skok")
    print("3 - atak")
    wybor = int(input())


def skok():
    skok = random.choices([1, 2, 3], [0.5, 0.3, 0.2])[0]
    print(f"Długość skoku: {skok}")
    return skok

def mega_skok():
    mega_skok = random.choices([5, -1], [0.3, 0.7])[0]
    if mega_skok == 5:
        print("Kozica wykonała mega skok!")
    else:
        print("Mega skok się nie udał, kozica cofa się o 1 pole.")
    return mega_skok

def atak(poz_1, poz_2):
    atak = random.randint(0, 1)

def przesuniecie(akcja, kolej, poz_1, poz_2):
    if kolej == 1:
        poz_1 += akcja
    if kolej == 2:
        poz_2 += akcja
    
    return poz_1, poz_2

def drukowanie_poz(poz_1, poz_2):
    print(f"Pozycja kozicy 1: {poz_1}")
    print(f"Pozycja kozicy 2: {poz_2}")

def main():
    random.seed(2020)
    
    poz_1 = 0
    poz_2 = 0
    kolej = 1
    
    while True:
        print(f"Ruch kozicy {kolej}.")
        ruch = ruch()
        if ruch == 1:
            akcja = skok()
        elif ruch == 2:
            akcja = mega_skok()
        elif ruch == 3:
            akcja = atak(poz_1, poz_2)

        poz_1, poz_2 = przesuniecie(akcja, kolej, poz_1, poz_2)
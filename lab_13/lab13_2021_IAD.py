'''class Zamowienie:
    __slots__ = {"towary"}

    def __init__(self, L=None):
        self.towary = []
        if isinstance(L, list):
            T = [None for _ in range(21)]
            max_idx = 0

            for idx_towaru, l_sztuk in L:
                if not (
                    isinstance(idx_towaru, int) and isinstance(l_sztuk, int | float),
                    0 <= idx_towaru <= 20 and l_sztuk > 0,
                ):
                    raise Exception("Bledne dane")
                T[idx_towaru] = l_sztuk
                max_idx = max(max_idx, idx_towaru + 1)

            self.towary = T[:max_idx]'''
class Zamowienie:
    cena = [i + 1 for i in range(21)]
    
    def __init__(self, lista=None):
        if lista is None:
            self.towary = []
            return

        max_indeks = 0
        self.towary = [0] * 21
        for i in range(len(lista)):
            if type(lista[i][0]) != int or not (0 <= lista[i][0] <= 20):
                raise Exception("Złe dane")
            if type(lista[i][1]) != int or not (0 <= lista[i][1]):
                raise Exception("Złe dane")

            self.towary[lista[i][0]] = lista[i][1]
            if max_indeks < lista[i][0]:
                max_indeks = lista[i][0]

        self.towary = self.towary[:max_indeks + 1]

    def __repr__(self):
        return 'Zamowienie(towary = ({self.towary})'

    def __str__(self):
        string = 'towar:'
        n = len(self.towary)
        for i in range(n):
            string += f'{i:>3}'
        string += '\nsztuk:'
        
        for i in range(n):
            string += f'{self.towary[i]:>3}'
        return string

    def oblicz_wartosc(self):
        return sum(self.cena[:len(self.towary)])

    def __lt__(self, other):
        c1 = self.oblicz_wartosc()
        assert isinstance(other, Zamowienie)
        c2 = other.oblicz_wartosc()
        
        return c1 < c2
    
    def __add__(self, other):
        if isinstance(other, Zamowienie):
            n = max(len(self.towary), len(other.towary))
            L = [(i, 0) for i in range(n)]
            suma = Zamowienie(L)
            for i in range(n):
                if i < len(self.towary) and i < len(other.towary):
                    suma.towary[i] = self.towary[i] + other.towary[i]
                elif i >= len(self.towary) and i < len(other.towary):
                    suma.towary[i] = other.towary[i]
                elif i >= len(other.towary) and i < len(self.towary):
                    suma.towary[i] = self.towary[i]
        
        elif isinstance(other, tuple):
            n = max(len(self.towary), other[0] + 1)
            L = [(i, 0) for i in range(n)]
            suma = Zamowienie(L)
            
            for i in range(len(self.towary)):
                suma.towary[i] = self.towary[i]
            suma.towary[other[0]] += other[1]

        return suma


    def __iadd__(self, other):
        if isinstance(other, Zamowienie):
            for i in range(len(other.towary)):
                if i < len(self.towary):
                    self.towary[i] += other.towary[i]
                else:
                    self.towary.append(other.towary[i])
        
        elif isinstance(other, tuple):
            if other[0] > len(self.towary) - 1:
                for i in range(other[0] - len(self.towary) + 1):
                    self.towary.append(0)
            self.towary[other[0]] += other[1]

        return self

def main():
    ##################### ETAP1 #####################
    print("## ETAP1: STWORZENIE KLASY, KONSTRUKTOR (2 PUNKTY) ##")
    zamowienie1 = Zamowienie([(1, 9), (3, 5), (4, 2), (7, 4), (0, 1)])
    zamowienie2 = Zamowienie([(0, 5), (4, 7), (19, 8), (7, 1)])
    zamowienie3 = Zamowienie()
    print(zamowienie1.towary)
    print(zamowienie2.towary)
    print(zamowienie3.towary)

    ##################### ETAP2 #####################
    print("\n## ETAP2: WYPISYWANIE (1 PUNKT) ##")
    print(zamowienie1.__repr__())
    print(zamowienie1.__str__())

    ##################### ETAP3 #####################
    print("\n## ETAP3: OBLICZANIE CENY, PORÓWNYWANIE (2 PUNKTY) ##")
    print(f"Ceny: {Zamowienie.cena}")
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"Cena zamowienie1: {zamowienie1.oblicz_wartosc()}")
    
    print(f"zamowienie2:\n{zamowienie2}")
    print(f"Cena zamowienie2: {zamowienie2.oblicz_wartosc()}")
    
    print(f"zamowienie1 < zamowienie2: {zamowienie1 < zamowienie2}")

    ##################### ETAP4 #####################
    print("\n## ETAP4: DODAWANIE ##")
    print("## Zamowienie + Zamowienie (2 PUNKTY) ##\n")
    
    print("zamowienie3 = zamowienie1 + zamowienie2")
    zamowienie3 = zamowienie1 + zamowienie2
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie2:\n{zamowienie2}")
    print(f"zamowienie3:\n{zamowienie3}")
    
    print("\n## Zamowienie + tuple (2 PUNKTY) ##\n")
    print("zamowienie4 = zamowienie1 + (0, 3)")
    zamowienie4 = zamowienie1 + (0, 3)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie4:\n{zamowienie4}")
    
    print("\nzamowienie5 = zamowienie1 + (17, 5)")
    zamowienie5 = zamowienie1 + (17, 5)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie5:\n{zamowienie5}")

    print("\n## += (1 PUNKT) ## \n")
    print("zamowienie1 += Zamowienie([(9, 3), (2, 5)])")
    zamowienie1 += Zamowienie([(9, 3), (2, 5)])
    print(f"zamowienie1:\n{zamowienie1}")
    
    print("\nzamowienie1 += (5, 9)")
    zamowienie1 += (5, 9)
    print(f"zamowienie1:\n{zamowienie1}")


if __name__ == "__main__":
    main()

import copy

def zamien_litere_na_liczbe(self, litera):
    return ord(litera.upper()) - ord('A')

def zamien_liczbe_na_litere(self, liczba):
    return chr(liczba + ord('A'))

class Samolot:
    def __init__(self, nazwa, l_rzedow, ile_miejsc_w_rzedzie):
        self.nazwa = nazwa
        self.l_rzedow = l_rzedow
        self.ile_miejsc_w_rzedzie = ile_miejsc_w_rzedzie
        self.stan_miejsc = [[0] * ile_miejsc_w_rzedzie for _ in range(l_rzedow)]  
        self.ilosc_miejsc = l_rzedow * ile_miejsc_w_rzedzie  
    
    def __repr__(self):
        druk = '  '
        for i in range(self.ile_miejsc_w_rzedzie):
            druk += zamien_liczbe_na_litere(self, i) + ' '
        druk += '\n'
        
        for i in range(self.l_rzedow):
            druk += str(i + 1) + '  '
            for j in range(self.ile_miejsc_w_rzedzie):
                druk += str(self.stan_miejsc[i][j]) + ' '
            druk += '\n'
        
        return f"{self.nazwa}\n {druk}"

    def rezerwuj_miejsce(self, miejsce):
        rzad = int(miejsce[0]) - 1
        id_miejsca = zamien_litere_na_liczbe(self, miejsce[1])
        if self.stan_miejsc[rzad][id_miejsca] != 1:
            self.ilosc_miejsc -= 1
            self.stan_miejsc[rzad][id_miejsca] = 1
            return True
        else:
            return False
        

    def sprawdz_czy_miejsce_wolne(self, miejsce):
        rzad = int(miejsce[0]) - 1
        id_miejsca = zamien_litere_na_liczbe(self, miejsce[1])
        if self.stan_miejsc[rzad][id_miejsca] == 0:
            return True
        else:
            return False

    def ilosc_wolnych_miejsc(self):
        return self.ilosc_miejsc

    def skopiuj_samolot_z_rezerwacjami(samolot, nowa_nazwa):
        kopia = Samolot(nowa_nazwa, samolot.l_rzedow, samolot.ile_miejsc_w_rzedzie)
        kopia.stan_miejsc = copy.deepcopy(samolot.stan_miejsc)
        return kopia

    def __sub__(self):
    
    def zamien_litere_na_liczbe(self, litera):
        return ord(litera.upper()) - ord('A')

    def zamien_liczbe_na_litere(self, liczba):
        return chr(liczba + ord('A'))  

            

def main():
    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)
    
    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    print(f"Rezerwacja miejsca 2b zakończkona: {airbus.rezerwuj_miejsce('2b')}")
    print(f"Rezerwacja miejsca 3C zakończkona: {airbus.rezerwuj_miejsce('3C')}")
    print(f"Rezerwacja miejsca 4D zakończkona: {airbus.rezerwuj_miejsce('4D')}")
    print(f"Rezerwacja miejsca 5C zakończkona: {airbus.rezerwuj_miejsce('5C')}")
    print(f"Rezerwacja miejsca 4B zakończkona: {airbus.rezerwuj_miejsce('4B')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    assert not airbus.sprawdz_czy_miejsce_wolne('3A'), 'Miejsce dopiero zostało zarezerwowane'
    assert airbus.sprawdz_czy_miejsce_wolne('4C'), 'Miejsce jeszcze nie zostało zarezerwowane'
    print()
    print(airbus)
    
    print(f'Ilość wolnych miejsc w samolocie to: {airbus.ilosc_wolnych_miejsc()}')
    
    airbus_kopia = Samolot.skopiuj_samolot_z_rezerwacjami(airbus, 'Embraer 190+')
    print(f"Rezerwacja miejsca 1B zakończkona: {airbus_kopia.rezerwuj_miejsce('1B')}")
    print(f"Rezerwacja miejsca 1C zakończkona: {airbus_kopia.rezerwuj_miejsce('1C')}")
    print(f"Rezerwacja miejsca 1D zakończkona: {airbus_kopia.rezerwuj_miejsce('1D')}")
    assert airbus.sprawdz_czy_miejsce_wolne('1B'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1C'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1D'), "Kopia się nie udała"
    print(airbus)
    print(airbus_kopia)



if __name__ == '__main__':
    main()
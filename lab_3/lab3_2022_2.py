n = int(input("Podaj liczbę dni: "))
t = int(input("Podaj wartość t: "))

if n <= 6 or t % 2 != 2:
    raise ValueError("Błędne dane.")

magazyn = 0
magazyn_max = 5 * t
dzien = 0
cena_teraz = 0
cena_dzien_temu = 0
cena_2dni_temu = 0
s_zarobek = 0
n_zarobek = 0


while dzien < n:
    dzien += 1
    cena_dzien_temu, cena_2dni_temu = cena_teraz, cena_dzien_temu
    cena_teraz = int(input(f"Podaj cene cukru dnia {dzien}: "))

    if cena_teraz <= 0:
        raise ValueError("Błędne dane.")
    
    if cena_teraz < cena_dzien_temu and cena_teraz < cena_2dni_temu:
        n_kupiono = 2 * t
        magazyn += n_kupiono
    else:
        n_kupiono = t / 2
        magazyn += n_kupiono
    if magazyn > magazyn_max:
        magazyn = magazyn_max

    n_sprzedaż = t / 2
    if cena_teraz > cena_dzien_temu > cena_2dni_temu:
        n_sprzedaż += (cena_teraz - cena_2dni_temu) / cena_2dni_temu * 5 * t
    
    if magazyn >= n_sprzedaż:
        magazyn -= n_sprzedaż
    else:
        n_sprzedaż = n_magazyn
        n_magazyn = 0
    
    s_zarobek += t * 0.15
    n_zarobek
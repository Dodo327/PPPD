import math

def main():
    r = int(input("Podaj rok urodzenia: "))
    while not r > 1900: 
        print("Niepoprawna data")
        r = int(input("Podaj rok urodzenia: ")) 
    
    m = int(input("Podaj miesiąc urodzenia: "))
    while not (m >= 1 and m <= 12):
        print("Niepoprawna data")
        m = int(input("Podaj miesiąc urodzenia: "))
    
    d = int(input("Podaj dzień urodzenia: "))
    while True:
        if m in {1, 3, 5, 7, 8, 10, 12} and (d >= 1 and d<= 31):
            break
        elif m in {4, 6, 9, 11} and (d >= 1 and d<= 31):
            break
        elif m == 2 and (r % 4 != 0 or (r % 400 != 0 and r % 100 == 0)) and (d >= 1 and d <= 28): 
            break
        elif m == 2 and ((r % 4 == 0 and r % 100 != 0) or r % 400 == 0) and (d >= 1 and d <= 29):
            break
        else:
            print("Niepoprawna data")
            d = int(input("Podaj dzień urodzenia: "))
    
    
    if m in { 4, 5} or (m == 6 and d <= 21) or (m  == 3 and d >= 21):
        print("Urodziłeś się w wiosnę")
    
    if m in { 7, 8} or (m == 9 and d <= 22) or (m  == 6 and d >= 22):
        print("Urodziłeś się w lato")
    
    if m in { 10, 11} or (m == 12 and d <= 22) or (m  == 9 and d >= 23):
        print("Urodziłeś się w jesień")
    
    if m in { 1, 2} or (m == 3 and d <= 21) or (m  == 12 and d >= 23):
        print("Urodziłeś się w zimę")

    if m in {1, 2}:
        m += 12
        r -= 1
    t = (d + math.floor(2.6 * (m - 2) - 0.2) + (r % 100) + math.floor((r % 100) / 4) + math.floor((r // 100) / 4) - 2 * (r // 100)) % 7
    dni_tyg = ['niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota']
    print('Był to', dni_tyg[t])

    m -= 12
    r += 1
    
    while True:
        r_r = int(input("Podaj rok referencyjny: "))
        while not r_r > 1900: 
            print("Niepoprawna data")
            r_r = int(input("Podaj rok referencyjny: ")) 
        
        m_r = int(input("Podaj miesiąc referencyjny: "))
        while not (m_r >= 1 and m_r <= 12):
            print("Niepoprawna data")
            m_r = int(input("Podaj miesiąc referencyjny: "))
        
        d_r = int(input("Podaj dzień referencyjny: "))
        while True:
            if m_r in {1, 3, 5, 7, 8, 10, 12} and (d_r >= 1 and d_r <= 31):
                break
            elif m_r in {4, 6, 9, 11} and (d_r >= 1 and d_r <= 31):
                break
            elif m_r == 2 and (r_r % 4 != 0 or (r_r % 400 != 0 and r_r % 100 == 0)) and (d_r >= 1 and d_r <= 28): 
                break
            elif m_r == 2 and ((r_r % 4 == 0 and r_r % 100 != 0) or r_r % 400 == 0) and (d_r >= 1 and d_r <= 29):
                break
            else:
                print("Niepoprawna data")
                d_d = int(input("Podaj dzień referencyjny: "))

        if r < r_r:            
            break
        elif r == r_r and m < m_r:   
            break
        elif r == r_r and m == m_r and d <= d_r:
            break
        print("Data refrencyjna nie może być przed datą urodzenia.")

    r_d = r_r - r
    m_d = m_r - m
    d_d = d_r - d    

    if d_d < 0:
        if m in {1, 3, 5, 7, 8, 10, 12}:
            d_d += 31
        elif m in {4, 6, 9, 11}:
            d_d += 30
        elif m == 2 and (r % 4 != 0 or (r % 400 != 0 and r % 100 == 0)): 
            d_d += 28
        elif m == 2 and ((r % 4 == 0 and r % 100 != 0) or r % 400 == 0):
            d_d += 29
          
           
        m_d -=1

    if m_d < 0:
        m_d += 12
        r_d -= 1

    print(f'Masz {r_d} lat, {m_d} miesięcy i {d_d} dni.')    




if __name__ == "__main__":
    main()
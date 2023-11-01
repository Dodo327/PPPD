import random

def rzucaj(L, p):
    l = L[random.randint(0, p - 1)]
    rzuty = [None] * l
    for i in range(l):
        rzuty[i] = random.randint(1, 6)

    return rzuty

def sprawdz(rzuty, n):
    ruch = 0
    poprzedni = 0
    for i in range(len(rzuty)):
        if rzuty[i] % 2 == 0:
            ruch += rzuty[i]
            
        elif rzuty[i] % 2 == 1:
            if poprzedni % 2 == 0:
                ruch -= rzuty[i]
                
            else:
                rzut = random.randint(1, 6)
                rzuty[i] = rzut
                if rzut % 2 == 0:
                    ruch += rzut
                else:
                    ruch -= rzut
                
        poprzedni = rzuty[i]
    if ruch >= n:
        return True, ruch
    
    return False, ruch

def main():
    random.seed(9876)
    n = 30
    p = 12
    L = [random.randrange(12, 40, 2) for _ in range(p)]
    
    proba = 1
    sukces = [None] * p
    proby = [None] * p 
    while proba <= p:
        rzuty = rzucaj(L, p)
        sukces[proba - 1] , ruch = sprawdz(rzuty, n)
        proby[proba - 1] = ruch
        
        print(f'Próba nr {proba}.')
        print('Rzuty:', rzuty)
        
        pozostałe = n - ruch
        if pozostałe < 0:
            pozostałe = 0
        
        print(f'Wykonując {len(rzuty)} rzutów udało się wykonać {ruch} kroków. Do pokonania zostało {pozostałe} kroków.')


        proba += 1
    
    print("Kroki pokonane we wszystkich próbach:", proby)
    print("Sukces każdej z prób:", sukces)

if __name__ == '__main__':
    main()
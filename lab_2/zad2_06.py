import math

def main():
    a = int(input())
    b = int(input())
    pierwsze = []

    if b < a:
        a, b = b, a

    for i in range(a, b + 1):
        dzielniki = False
        if i < 1:
            continue

        for j in range(2, int(math.sqrt(i)) + 1):
            if  i % j == 0:
                dzielniki = True
                break
        
        if not dzielniki and i != 1:
            pierwsze.append(i)
            
    print("liczby pierwsze:", pierwsze)
    print('jest ich', len(pierwsze))





if __name__ == '__main__':
    main()
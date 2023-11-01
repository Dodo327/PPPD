import random
import math

def przyblizPi(n):
    licznik = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            licznik += 1
    
    return licznik * 4 / n

def main():
    for i in range(1, 7):
        pi = przyblizPi(10 ** i)
        print(pi, 'róznica:', abs(math.pi - pi))
     


if __name__ == '__main__':
    main()
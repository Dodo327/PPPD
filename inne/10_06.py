import time
import random

def merge(x, y):
    u = []
    v = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                u.append(i)
                v.append(j)
    return [u, v]                

def merge_sorted(x, y):
    u = []
    v = []
    j = 0 
    for i in range(len(x)):
        for z in range(j, len(y)):
            if y[z] > x[i]:
                j += 1
                break
            if x[i] == y[z]:
                u.append(i)
                v.append(z)
    return [u, v]
    
def main():
    x = []
    y = []
    for i in range(100):
        x.append(random.randint(1, 100))
        y.append(random.randint(1, 100))
    
    print(x)
    print(y)

    st = time.time()
    print(merge(x, y))
    kon = time.time()
    print(kon - st)

    x.sort()
    y.sort()

    st = time.time()
    print(merge_sorted(x, y))
    kon = time.time()
    print(kon - st)

if __name__ == '__main__':
    main()
import math

# cx = float(input("Podaj wartość cx: "))
# cy = float(input("Podaj wartość cy: "))
# x0 = float(input("Podaj wartość x0: "))
# y0 = float(input("Podaj wartość y0: "))
# szerokość = float(input("Podaj szerokość badanego obrazu: "))
# rozdzielczość = int(input("Podaj rozdzielczość wizualizacji: "))
# max_iteracji = int(input("Podaj maksymalną ilość iteracji dla jednego punktu: "))

cx = -0.123
cy = 0.745
x0 = y0 = 0
szerokość = 2
rozdzielczość = 31
max_iteracji = 25

if szerokość <= 0 or rozdzielczość <= 0 or max_iteracji < 0 or rozdzielczość % 2 == 0:
    raise ValueError("Błędne dane!")

l_iteracji = 0
l_iteracji_całość = 0
x, y = x0, y0
dist = math.sqrt(x ** 2 + y ** 2)

print(f"Trajektoria punktu ({x}, {y}):")
while l_iteracji < max_iteracji and dist < 2:
    x, y = x ** 2 - y ** 2 + cx, 2 * x * y + cy 
    print(f"({x}, {y})")
    l_iteracji += 1
    dist = math.sqrt(x ** 2 + y ** 2)

l_iteracji_całość += l_iteracji
for i in range(rozdzielczość):
    for j in range(rozdzielczość):
        x1, y1 = x0 + j * (szerokość / (rozdzielczość - 1)) - szerokość / 2, y0 - i * (szerokość / (rozdzielczość - 1)) + szerokość / 2
        l_iteracji = 0
        dist = math.sqrt(x1 ** 2 + y1 ** 2)
        
        while l_iteracji < max_iteracji and dist <= 2:
            x1, y1 = x1 ** 2 - y1 ** 2 + cx, 2 * x1 * y1 + cy
            l_iteracji += 1
            dist = math.sqrt(x1 ** 2 + y1 ** 2)
            if dist > 2:
                break
        
        l_iteracji_całość += l_iteracji
        if dist <= 2:
            print("@", end='')
        else:
            print(" ", end='')
    print()    
    
    


print(f'Program przeprowadził {l_iteracji_całość} iteracji')
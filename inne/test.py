import random
x = 0
y = 1
for i in range(100000):
    z = random.random()
    if z > x:
        x =z
    if z<y:
        y = z

print(x, y)
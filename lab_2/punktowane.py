def main():
    width = int(input("Podaj szerokość: "))
    height = int(input("Podaj wysokość: "))

    x = float(input("Podaj współrzędną x piłki: "))
    y = float(input("Podaj współrzędną y piłki: "))
    vx = float(input("Podaj współrzędną x prędkości piłki: "))
    vy = float(input("Podaj współrzędną y prędkości piłki: "))

    t = float(input("Podaj czas symulacji: "))
    t_now = 1

    if height < 0 or width < 0 or x < 0 or x > width or y < 0 or y > height or t < 0 or vx == 0 or vy == 0:
        raise ValueError("Błędne dane!")

    while t_now <= t:
        x += vx
        if x > width:
            x = width - (x - width)
            vx *= -1
        elif x < 0:
            x *= -1
            vx *= -1
        
        y += vy
        if y > height:
            y = height - (y - height)
            vy *= -1
        elif y < 0:
            y *= -1
            vy *= -1

        t_now += 1

    print(f"Na koniec symulacji piłka znajduje się w punkcie ({x}, {y})")

    print("Stan planszy po zakończeniu symulacji:")
    for i in range(height, -1, -1):
        for j in range(0, width + 1):
            if i == round(y) and j == round(x):
                print("0", end='')
            elif i == 0 or i == height:
                print("#", end='')
            elif j == 0 or j == width:
                print("#", end='')
            else:
                print(' ', end='')

            if j == width:
                print()
            

if __name__ == "__main__":
    main()

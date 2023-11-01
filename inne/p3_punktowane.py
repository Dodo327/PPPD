def main(): 
    width = int(input("Podaj szerokość: "))
    height = int(input("Podaj wysokość: "))

    x = float(input("Podaj współrzędną x piłki: "))
    y = float(input("Podaj współrzędną y piłki: "))
    vx = float(input("Podaj współrzędną x prędkości piłki: "))
    vy = float(input("Podaj współrzędną y prędkości piłki: "))

    t = float(input("Podaj czas symulacji: "))
    t_now = 0

    if width < 0 or height < 0 or (x < 0 or x > width) or (y < 0 or y > height) or (vx == 0 and vy == 0) or t < 0:
        raise ValueError("Błędne dane!")

    while t_now < t:
        if vx > 0:
            t_do_ściany_x = (width - x) / vx
        elif vx < 0:
            t_do_ściany_x = (- x) / vx
        else:
            t_do_ściany_x = ('inf')
        
        if vy > 0:
            t_do_ściany_y = (height - y) / vy
        elif vy < 0:
            t_do_ściany_y = (- y) / vy
        else:
            t_do_ściany_y = ('inf')

        if t_do_ściany_x < t_do_ściany_y:
            if t_now + t_do_ściany_x <= t:
                x += vx * t_do_ściany_x
                y += vy * t_do_ściany_x
                vx *= -1
                t_now += t_do_ściany_x
                print(f"Piłka odbija się od ściany w punkcie ({x}, {y}) i t = {t_now}.")
            else:
                x += vx * (t - t_now)
                y += vy * (t - t_now)
                t_now = t
        elif t_do_ściany_y < t_do_ściany_x:
            if t_now + t_do_ściany_y <= t:
                x += vx * t_do_ściany_y
                y += vy * t_do_ściany_y
                vy *= -1
                t_now += t_do_ściany_y
                print(f"Piłka odbija się od ściany w punkcie ({x}, {y}) i t = {t_now}.")
            else:
                x += vx * (t - t_now)
                y += vy * (t - t_now)
                t_now = t
        else:
            if t_now + t_do_ściany_y <= t:
                x += vx * t_do_ściany_y
                y += vy * t_do_ściany_y
                vx *= - 1
                vy *= -1
                t_now += t_do_ściany_y
                print(f"Piłka odbija się od ściany w punkcie ({x}, {y}) i t = {t_now}.")
            else:
                x += vx * (t - t_now)
                y += vy * (t - t_now)
                t_now = t
        
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
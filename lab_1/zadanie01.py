def main():
    x = int(input("Ile schodów przeszedłeś? "))

    if 0 <= x <= 300:
        if x % 15 == 0:
            p = int(x / 15)
            print("Jesteś na pietrze nr " + str(p))

        else:
            p = (x//15)
            print(f"Jesteś pomiedzy pietrami {p} i {p+1}")

        if x % 30 > 15:
            print(f"Masz {30 - (x % 30)} schodków w góre do toalety")

        elif x % 30 < 15:
            print(f"Masz {x % 30} schodków w dół do toalety")

        elif x % 30 == 15:
            print("Masz 15 schodków w górę lub w dół do toalety")

        else:
            print(f"Masz {x % 30} schodków do toalety")

    else:
        print("Błędne dane")


if __name__ == "__main__":
    main()

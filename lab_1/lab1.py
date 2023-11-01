def main():
    print("moj pierwszy program")
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))

    print(f'suma to {a + b}')
    print('suma to', a + b, end=' ', sep='_')
    print('suma to ' + str(a + b))


if __name__ == "__main__":
    main()

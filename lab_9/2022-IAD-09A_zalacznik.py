def wypisz_macierz(M):
    for j in range(len(M[0]) + 2):
        print("-", end="")

    print()

    for i in range(len(M) - 1, -1, -1):
        print("|", end="")
        for j in range(len(M[i])):
            if M[i][j]:
                print("#", end="")
            else:
                print(" ", end="")
        print("|")

    for j in range(len(M[0]) + 2):
        print("-", end="")
    print()
import math

def read_data(datafile):
    extracted_data = [i.strip().split() for i in open(datafile)]
    flat_list = [int(item) for sublist in extracted_data for item in sublist]
    return flat_list

def validate(d, n, x):
    if not d < n:
        raise ValueError(("Błędne dane"))

    if not x <= n - 1:
        raise ValueError(("Błędne dane"))

def merge_islands(flat_list):
    for i in range (1, len(flat_list) - 1, 2): #sprawdzamy czy wyspy nachodzą na siebie
        if flat_list[i] >= flat_list[i + 1]: #jeśli tak to koniec pierwszej i pocz drugiej wyspy zmieniamy na nan
            flat_list[i], flat_list[i + 1] = math.nan, math.nan

    length = 0
    for i in range(0, len(flat_list)): #określamy długość list scalonych wysp
        if not math.isnan(flat_list[i]): 
            length += 1

    merged_islands = [math.nan] * length
    for j in range(0, length): # uzupełniamy listę scalonych wysp o wspołrzędne które != nan
        for i in range(0, len(flat_list)):
            if not math.isnan(flat_list[i]) and math.isnan(merged_islands[j]):
                merged_islands[j] = flat_list[i]
                flat_list[i] = math.nan
                break

    return merged_islands

def create_map(merged_islands, n, d):
    map = ['_'] * n #wypełniamy wyspe morzem
    for i in range(0, len(merged_islands) - 1, 2):
        for j in range(merged_islands[i], merged_islands[i + 1] + 1):
            map[j] = '|' #dodajemy wyspy według ich współrzędnych
            for m in range(merged_islands[i] - d, merged_islands[i + 1] + d + 1):
                if 0 < m < n and map[m] != '|': 
                    map[m] = '-' #w odległości d od wysp dodajemy rafy jesli mieszczą się na mapie i nie nachodzą na wyspę
    return map

def main():
    d = int(input(("Podaj liczbę d definiującą odległość, na jaką każda wyspa będzie okalana przez rafę koralową: ")))
    n = int(input("Podaj liczbę n, określająca długość naszej mapy: "))
    file_name = '2021-MAT-07_koordynaty_wysp.csv'
    flat_list = read_data(file_name)
    
    validate(d, n, flat_list[len(flat_list) - 1])
    merged_islands = merge_islands(flat_list)

    map = create_map(merged_islands, n, d)
    print(map)

if __name__ == '__main__':
    main()
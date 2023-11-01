import math
import random

def print_header():
    print("Wybierz opcję co chcesz zrobić:")
    print("1 - wylosuj początek przedziału\n2 - wylosuj koniec przedziału\n3 - Zapisz wyliczenia do pliku\n4 - wczytaj stan z pliku\n5 - wyjdź z programu")

def read_action():
    action = int(input("Podaj akcję którą chcesz wykonać: "))
    
    while action not in (1 , 2, 3, 4, 5):
        print(f"Wprowadziłeś nieprawidłową wartość: {action}")
        action = int(input("Podaj akcję którą chcesz wykonać: "))
    
    return action

def generate_beginning(order_of_magnitude):
    beginning = math.nan
    
    while order_of_magnitude > 0:
        if math.isnan(beginning):
            beginning = random.randint(1, 6)
        else:
            beginning = beginning * 10 + random.randint(1, 6)
        order_of_magnitude -= 1
    
    return beginning

def generate_end(order_of_magnitude):
    order_of_magnitude += 1
    end = math.nan
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    chance = [0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05]
    
    while order_of_magnitude > 0:
        if math.isnan(end):
            end = random.choices(choice, chance, k = 1)[0]
        else:
            end = end * 10 + random.choices(choice, chance, k = 1)[0]
        order_of_magnitude -= 1
    
    return end

def concatenate_abundants_from_range(beginning, end):
    if math.isnan(beginning) or math.isnan(end):
        return math.nan

    number = 0
    for i in range(beginning, end + 1):
        suma_dzielniki = 0
        
        for j in range(1, i):
            if i % j == 0:
                suma_dzielniki += j

        if suma_dzielniki > i:
            number = number * 10 ** (1 + int(math.log10(i))) + i
    
    return number

def save_file(beginning, end, number, order_of_magnitude):
    
    if math.isnan(beginning) or math.isnan(end) or math.isnan(number) or math.isnan(order_of_magnitude):
        print("Wymagane dane nie są wypełnione")
    else: 
        path = input("Podaj nazwę pliku do odczytu: ")
        with open(path, 'w') as file:
            print(beginning, end, number, order_of_magnitude, sep="\n", file = file)
        
        print(f"Dane zostały zapisane do pliku: {path}")

def read_from_file():
    find_path = input("Podaj nazwę pliku do odczytu: ")
    answer = []
    with open(find_path, "r") as file:
        for line in file:
            answer.append(line)

    return answer[0], answer[1], answer[2], answer [3]

def main():
    random.seed(2014)
    #order_of_magnitude = random.choices([1, 2], [0.6, 0.4], k = 1)[0]
    order_of_magnitude = 1
    print(f"Początek przedziału będzie {order_of_magnitude}-cyfrowy")
    number = math.nan
    beginning = math.nan
    end = math.nan
    
    while True:
        print_header()
        action = read_action()
        """if action == 1:
            beginning = generate_beginning(order_of_magnitude)
        elif action == 2:
            end = generate_end(order_of_magnitude)
        elif action == 3:
            save_file(beginning, end, number, order_of_magnitude)
        elif action == 4:
            read_from_file()"""
        beginning = 3
        end = 83
        number = concatenate_abundants_from_range(beginning, end)
        print(f"< {beginning} : {end} > => {number}")
        
        if action == 5:
            print("Wyjście")
            break



if __name__ == "__main__":
    main()
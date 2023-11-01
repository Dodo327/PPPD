import random
import os
import os.path

def generate_row():
    row_id = random.randint(0, 100000)
    
    login = ''
    previous_letter = None
    letter = None
    for i in range(5):
        previous_letter = letter
        while True:
            letter = number_to_letter(random.randint(0, 25))
            if letter != previous_letter:
                break
        login = join_letter(login, letter)

    level = random.choices(['beginner', 'regular', 'senior', 'expert'], [0.5, 0.3, 0.15, 0.05], k=1)[0]

    return row_id, login, level

def number_to_letter(number):
    return chr(number + ord('a'))

def join_letter(base, letter):
    return base + letter

def get_file_for_row(row_id, file0_exists, file1_exists, file2_exists):
    hash = row_id % 360
    
    if 0 <= hash < 120:
        if file0_exists:
            return 0
        elif not file0_exists and file2_exists:
            return 2
        elif not file0_exists and not file2_exists:
            return 1

    if 120 <= hash < 240:
        if file1_exists:
            return 1
        elif not file1_exists and file0_exists:
            return 0
        elif not file1_exists and not file0_exists and file2_exists:
            return 2

    if 240 <= hash < 360:
        if file2_exists:
            return 2
        elif not file2_exists and file1_exists:
            return 1
        elif not file2_exists and not file1_exists and file0_exists:
            return 0

def save_row_in_file(file_name, row_id, login, level):
    with open(file_name, "a") as file:
        print(row_id, login, level, sep=' ', file = file)

def can_delete_file(file_id, file0_exists, file1_exists, file2_exists):
    if file_id == 0:
        if file0_exists and (file1_exists or file2_exists):
            return True
        else:
            return False
    
    if file_id == 1:
        if file1_exists and (file0_exists or file2_exists):
            return True
        else:
            return False

    if file_id == 2:
        if file2_exists and (file0_exists or file1_exists):
            return True
        else:
            return False

def remove_file(file_id, file0_exists, file1_exists, file2_exists):
    
    if file_id == 0:
        with open('file0.txt', 'r') as file0:
            for line in file0:
                if file2_exists:
                    with open('file2.txt', 'a') as file2:
                        file2.write(line)
                else:
                    with open('file1.txt', 'a') as file1:
                        file1.write(line)
        remove_file_from_disk('file0.txt')
        
    
    if file_id == 1:
        with open('file1.txt', 'r') as file1:
            for line in file1:
                if file0_exists:
                    with open('file0.txt', 'a') as file0:
                        file0.write(line)
                else:
                    with open('file2.txt', 'a') as file2:
                        file2.write(line)
        remove_file_from_disk('file1.txt')
        
    if file_id == 2:
        with open('file2.txt', 'r') as file2:
            for line in file2:
                if file1_exists:
                    with open('file1.txt', 'a') as file1:
                        file1.write(line)
                else:
                    with open('file0.txt', 'a') as file0:
                        file0.write(line)
        remove_file_from_disk('file2.txt')
        


def remove_file_from_disk(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def get_file_name(file_id):
    """Zwraca nazwę pliku na podstawie identyfikatora pliku"""
    return f"file{file_id}.txt"

def print_files_state(files_count=3):
    """Wypisuje stan plików"""
    for file_id in range(files_count):
        file_name = get_file_name(file_id)
        if not os.path.exists(file_name):
            continue
        content = ''
        with open(file_name, "r") as read_file:
            print(f'{file_name}: ')
            content = read_file.read()
        
        if content.strip() !='':
            print(content.strip())

def main():
    random.seed(2022)
    file0_exists = True
    file1_exists = True
    file2_exists = True
    row_id, login, level = None, None, None
    
    while True:
        
        print("Możliwe akcje to:")
        print("1 - Wygeneruj wiersz danych")
        print("2 - Zapisz wygenerowany uprzednio wiersz do odpowiedniego pliku.")
        print("3 - Usuń plik o podanym id (0-2)")
        print("4 - Wyjdź z program")
        action = int(input("Podaj nr akcji do wykonania: "))

        if action == 1:
            row_id, login, level = generate_row()
            print(f"Wygenerowano wiersz: row_id: {row_id}, login: {login}, level: {level}")
        
        elif action == 2:
            if row_id == None:
                print("Najpierw trzeba wygenerować wiersz, aby go zapisać")
                continue
            
            file_id = get_file_for_row(row_id, file0_exists, file1_exists, file2_exists)
            if file_id == 0:
                file_name = 'file0.txt'   
            elif file_id == 1:
                file_name = 'file1.txt'
            elif file_id == 2:
                file_name = 'file2.txt'
            
            print(f"Wiersz zapisany do {file_name}")
            save_row_in_file(file_name, row_id, login, level)
            print_files_state(files_count=3)

            row_id, login, level = None, None, None

        elif action == 3:
            file_id = int(input('Podaj numer pliku do usunięcia: '))
            if file_id in (0, 1, 2):
                if can_delete_file(file_id, file0_exists, file1_exists, file2_exists):
                    remove_file(file_id, file0_exists, file1_exists, file2_exists)
                    print(f"Plik {file_id} został usunięty")
                    if file_id == 0:
                        file0_exists = False
                    elif file_id == 1:
                        file1_exists = False
                    elif file_id == 2:
                        file2_exists = False

                else:
                    print("Nie można usunąć pliku")
                
                

            else:
                print("Błędny nr pliku")
        
        elif action == 4:
            break

        else:
            print("Błędny nr akcji")
        
        


if __name__ == "__main__":
    main()
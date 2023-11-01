def main():
    width = 10
    height = int(input('Podaj wysokość ściany {7, 9, 11}: '))

    x_length = int(input('Podaj długość rolki x: '))
    o_length = int(input('Podaj długość rolki o: '))
    x_time = float(input('Podaj czas przyklejania jednej jednostki rolki x: '))
    x_left = x_length #ile nam zostało na rolce
    o_left = o_length
    x_count = 0 
    o_count = 0
    o_roll = True #czy używamy rolke o
    time = 0

    window_height = 3
    window_width = 3
    window_padding = 2


    if not(x_length > 0 and o_length > 0 and x_length < width - 1 and o_length <= x_length / 2):
        raise ValueError('Nieprawidłowe długości rolek')

    for i in range(0, height):
        for j in range(0, width):
            if i in range(height - (window_height + window_padding), height - window_padding) and j in range(width - (window_width + window_padding), width - window_padding):
                print(' ', end='')        
            elif o_roll:
                if o_left == o_length:
                    o_count += 1
                    time += 3 * x_time
                
                print('o', end='')
                o_left -= 1
                time += x_time / 3
                if o_left == 0:
                    o_roll = False
                    o_left = o_length
            else:
                if x_left == x_length:
                    x_count += 1                
                    time += 3 * x_time

                print('x', end='')
                x_left -= 1
                time += x_time
                if x_left == 0:
                    o_roll = True
                    x_left = x_length
            
            if j == width - 1:
                print()

    print(f"Tapetowanie zajęło {time} czasu.")
    print(f"Zużyto {x_count} rolek x i {o_count} rolek o.")

if __name__ == '__main__':
    main()
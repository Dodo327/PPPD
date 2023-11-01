import csv
import math

def read_csv(plik):
    data_frame = []
    with open(plik) as f:
        for row in csv.reader(f):
            data_frame.append([row[i] for i in range(len(row))])
    return data_frame

def print_data(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(f'{M[i][j]:^10}', end='')
        print()

def convert_rows_type(M, start, count):
    for i in range(1, len(M)):
        for j in range(start, start + count):
            M[i][j] = int(M[i][j])

def left_join(M1, M2):
    M3 = [[float('NaN') for _ in range(len(M1[0]) + len(M2[0]) - 1)] for i in range(len(M1))]

    for i in range(len(M1[0])):
        M3[0][i] = M1[0][i]
    for j in range(1, len(M2[0])):
        M3[0][j + len(M1[0]) - 1] = M2[0][j]
    
    for i in range(1, len(M3)):
        for j in range(len(M3[0])):
            if j < len(M1[0]):
                M3[i][j] = M1[i][j]
    
    for i in range(1, len(M3)):
        for k in range(1, len(M2)):
            if M2[k][0] == (M3[i][0]):
                for l in range(1, len(M2[0])):
                    M3[i][l + len(M1[0]) - 1] = M2[k][l]
            
    return M3

def summarize(M, start, count):
    pods = [[float('NaN')] * 4 for _ in range(len(M) - 1)]
    for i in range(len(pods)):
        pods[i][0] = M[i + 1][0]

    for j in range(len(pods)):
        suma = 0
        min_w = float('inf')
        for i in range(start, start + count):
            if math.isnan(M[j + 1][i]):
                min_w = 0
                continue
            else:
                if min_w > M[j + 1][i]:
                    min_w = M[j + 1][i]
                suma += M[j + 1][i]
        
        pods[j][1] = suma
        pods[j][2] = suma - min_w
        
        zal = (10 * (count - 1)) / 2
        if suma - min_w <= zal:
            pods[j][3] = 'nzal'
        else:
            pods[j][3] = 'zal'
    
    return pods

def main():
    M1 = read_csv('m1.csv')
    M2 = read_csv('m2.csv')
    
    convert_rows_type(M2, 1 , 7)
    M3 = left_join(M1, M2)
    
    print('Połączone:')
    print_data(M3)
    
    print('Podsumowanie:')
    print_data(summarize(M3, 3, 7))

if __name__ == '__main__':
    main()
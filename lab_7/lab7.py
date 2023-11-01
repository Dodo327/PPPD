def revert_in_subgroups(arr, sub_size):
    n = len(arr)
    for i in range(n):
        i = i % sub_size
        arr[i], arr[sub_size - i - 1] = arr[sub_size - i - 1], arr[i]

def sort_123(arr):
    n = len(arr)
            
        
def get_top_indexes(arr):
    n = len(arr)
    top_index_nr = 0
    
    for i in range(n):
        if i == 0:
            x0 = float('-inf')
        else:
            x0 = arr[i - 1]
        
        x1 = arr[i]
        
        if i == n - 1:
            x2 = float('-inf')
        else:
            x2 = arr[i + 1]

        if x0 < x1  and x1 > x2 :
            top_index_nr += 1

    top_indexes = [None] * top_index_nr
    top_index_nr = 0
    
    for i in range(n):
        if i == 0:
            x0 = - float('inf')
        else:
            x0 = arr[i - 1]
        
        x1 = arr[i]
        
        if i == n - 1:
            x2 = float('-inf')
        else:
            x2 = arr[i + 1]

        if x0 < x1 and x1 > x2:
            top_indexes[top_index_nr] = i
            top_index_nr += 1
        
    return top_indexes

def calculate_max_sum(arr):
    suma_max = - float('inf')
    n = len(arr)
    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += arr[j]
            if suma > suma_max:
                suma_max = suma
        
    return suma_max

def main():
    
    arr = [1, 2, 3, 4, 5]
    sub_size = 3
    revert_in_subgroups(arr, sub_size)
    print('revert_in_subgroups')
    print(arr)
    
    print('sort_123')
    s1 = [2, 1, 1, 1, 2, 3, 1, 2, 3, 3]
    
    
    print('get_top_indexes')
    print(get_top_indexes([8, 3, 4, 1, 1, 4, 4, 5]))
    print(get_top_indexes([0]))

    print('calculate_max_sum')
    print(calculate_max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(calculate_max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(calculate_max_sum([-2, -3, -5]))


if __name__ == "__main__":
    main()
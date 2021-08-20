from random import randrange

def fun_sort():
    # сортируем столбы по возрастанию сумм
    list_sum = [sum([matrix[index_col][i] for index_col in range(m)]) for i in range(m)]
    flag = True
    while flag:
        flag = False
        for i in range(m - 1):
            j = i + 1
            if list_sum[i] > list_sum[j]:
                list_sum[i], list_sum[j] = list_sum[j], list_sum[i]
                flag = True
                for line in range(m):
                    matrix[line][i], matrix[line][j] = matrix[line][j], matrix[line][i]
    # print(list_sum, '\n')
    # print(*matrix, list_sum, sep='\n')
    # сортруем элементы столбцов по условию
    for coll in range(m):
        if not coll % 2:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] < matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], matrix[i][coll]
                        flag = True
        else:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] > matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], matrix[i][coll]
                        flag = True
    print(*matrix, list_sum, sep='\n')


#m = 10
#matrix = [
#    [47, 48, 36, 12, 39, 33, 13, 1, 47, 20],
#    [17, 2, 9, 40, 2, 1, 36, 35, 48, 44],
#    [50, 24, 20, 29, 27, 49, 8, 50, 20, 32],
#    [30, 3, 17, 33, 43, 10, 17, 2, 42, 19],
#    [14, 5, 50, 38, 17, 18, 24, 26, 19, 24],
#    [12, 41, 45, 12, 4, 33, 33, 16, 36, 25],
#    [15, 27, 12, 30, 22, 36, 45, 46, 43, 21],
#    [46, 34, 34, 47, 22, 34, 45, 12, 47, 19],
#    [31, 47, 2, 1, 12, 45, 44, 26, 11, 23],
#    [25, 49, 47, 50, 36, 9, 36, 10, 21, 26],
#    ]
#print('До сортировки', end='\n')
#print(*matrix, sep='\n')
#print()
#fun_sort()
#print()
#print('После сортировки', end='\n')
#print(*matrix, sep='\n')

while True:
    m = input("Введите размер массива (m должен быть больше 5): ")
    if not str(m).isdigit() or int(m) <= 5:
        print('Введенное значение не удовлетворяет требованию. Значение должно быть целым числом больше 5.\n')
        continue
    else:
        break
m = int(m)
print(f'Исходный массив будет иметь размер М*М - {m}*{m}')

list_sum = []

matrix = [[randrange(1, 50) for i in range(m)] for _ in range(m)]

for n in range(len(matrix)):
    column_sum = 0
    for m in range(len(matrix[n])):
        column_sum += matrix[n][m]
    list_sum.append(column_sum)

print('До сортировки', end='\n')
print(*matrix, list_sum, sep='\n')
print()
print('После сортировки', end='\n')
fun_sort()

#print(*matrix, list_sum, sep='\n')
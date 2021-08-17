fun_1 = lambda x, y = 5: x ** y

print(fun_1(3))
print(fun_1(4, 7))

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [3, 4, 5, 5, 4, 3, 2, 2, 7]

print(list(map(fun_1, lst1)))

print(list(map(fun_1, lst1, lst2)))
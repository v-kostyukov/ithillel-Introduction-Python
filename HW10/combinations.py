def without_00(a, b):
    if a > b + 1:
        return 0
    if a == 0 or b == 0:
        return 1

    return without_00(a, b - 1) + without_00(a - 1, b - 1)


a = 2
b = 2
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))

print(without_00(a, b))

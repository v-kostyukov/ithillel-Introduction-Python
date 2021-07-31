n = int(input("Введите натуральное число: " ))
result = "Нет"
a1 = 0
a2 = 0

while n > 0:
    a1 = n % 10
    m = n // 10
    while m > 0:
        a2 = m % 10
        if a1 == a2:
            result = "Да"
        m = m // 10
    n = n // 10

print(result)
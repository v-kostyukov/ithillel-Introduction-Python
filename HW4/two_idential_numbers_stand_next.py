n = int(input("Введите натуральное число: " ))
result = "Нет"
a1 = 0
a2 = 0

while n > 0:
    a1 = n % 10
    a2 = n // 10 % 10
    if a1 == a2:
        result = "Да"
    n = n // 10

print(result)
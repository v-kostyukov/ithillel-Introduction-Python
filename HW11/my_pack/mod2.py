"""
Модуль содержит фун-ии:
    fun_check: Функция должна проверить есть ли в списке 2 числа сума которых
    еквивалентна числу переданому 2м параметром. Функция должна вернуть
    булевое значение - результат поиска фукции.
    Для проверки вызвать 2 раза функцию с разными тестовыми примерами.
    reverse_it: функция получает число, и возвращает его  в противоположном порядке.
    count_first: функция в которой каждое натуральное число k встречается ровно k раз: 1, 2, 2
"""

__all__ = ['fun_check', 'reverse_it']
__author__ = 'Vitaliy Kostyukov'


def fun_check(num, *args):
    num_list = args
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            if i != j and num_list[i] + num_list[j] == num:
                return True
    return False


def reverse_it(n, i=0):
    return i if (n == 0) else reverse_it(n // 10, i * 10 + n % 10)


def count_first(n: int) -> str:
    k = 1
    res = ''
    for i in range(1, n + 1):
        res = ' '.join([res, str(k)])
        if i == k * (k + 1) // 2:
            k += 1
    return res

"""
Модуль содержит фун-ии сортиворок последовательностей:
    bubble_sort: функция сотрировки методом пузырька
    bubble_rock_sort: функция сортировки методом камня
    insertion_sort: функция сортировки мметодом вставки
"""

# from random import *

__all__ = ['bubble_sort', 'bubble_rock_sort', 'insertion_sort']
__author__ = 'Vitaliy Kostyukov'


def bubble_sort(arr):

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_rock_sort(array):
    # пределим длину массива
    length = len(array)
    # Внешний цикл, кол-во проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length - i - 1):
            # Меняем элементы местами
            if array[j] < array[j + 1]:
                # temp = array[j]
                # array[j], = array[j+1]
                # array[j+1] = temp
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован

    # print(nums)
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1

        # Элементы отсортированного сегмента перемещен вперёд, если они больше элемента вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert

    return nums


# if __name__ == "__main__":
#    print()

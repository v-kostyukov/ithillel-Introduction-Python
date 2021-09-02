"""
Модуль содержит фун-ии:
    counts_unique_numbers: функция считает сколько уникальных чисел содержится одновременно как в 1 списке, так и во 2
    counts_numbers: функция считает сколько чисел содержится одновременно как в первом списке, так и во втором
    inverted_words: функция переворачивает слова и меняет их в порядке следования
"""

__all__ = ['counts_unique_numbers', 'counts_numbers', 'inverted_words']
__author__ = 'Vitaliy Kostyukov'


def counts_unique_numbers(a, b):
    # a = []  # Список a
    # b = []  # Список b

    # Считает сколько чисел содержится одновременно как в первом списке, так и во втором
    # print(len(set(a) & set(b)))

    # Считает сколько уникальных чисел содержится одновременно как в первом списке, так и во втором
    return len(list(x for x in (a + b) if (a + b).count(x) == 1))


def counts_numbers(a, b):
    # a = []  # Список a
    # b = []  # Список b

    return len(set(a) & set(b))


def inverted_words(words):
    # words = input("Введите два слова: ")

    return words[::-1].title()

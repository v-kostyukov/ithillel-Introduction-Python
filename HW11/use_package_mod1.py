from my_pack import mod1

a = [23, 44, 5, 21, 67]
b = [5, 18, 34, 67, 44]

words = input("Введите два слова: ")

print("Уникальных чисел содержится одновременно как в первом списке, так и во втором: ", mod1.counts_unique_numbers(a, b))
print("Кол-во чисел содержится одновременно как в первом списке, так и во втором: ", mod1.counts_numbers(a, b))
print("=>", mod1.inverted_words(words))






from my_pack import mod1

# help(mod1)

a = [23, 44, 5, 21, 67]
b = [5, 18, 34, 67, 44]

words = input("Введите два слова: ")

print("Ун-ых чисел содерж. од-но в 1, 2: ", mod1.counts_unique_numbers(a, b))
print("Кол-во чисел содержится од-но как в 1, 2: ", mod1.counts_numbers(a, b))
print("=>", mod1.inverted_words(words))

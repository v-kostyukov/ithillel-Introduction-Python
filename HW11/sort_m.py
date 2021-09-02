# from sortm import *
import sortm

lst = [45, 12, 7, 78, 1, 34, 15]

print("До сотрировки: ", lst)
print("После сортировки методом пузырька: ", sortm.bubble_sort(lst))
print("После сортировки методом камня: ", sortm.bubble_rock_sort(lst))
print("После сортировки методом вставки: ", sortm.insertion_sort(lst))

# print(help(sortm))
# print(dir(sortm))

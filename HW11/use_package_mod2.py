from my_pack import mod2

lst = [i for i in range(0, 12)]

print(lst)
print(mod2.fun_check(33, *lst))
print(mod2.fun_check(11, *lst))


n = int(input('Введите число n: '))

print(mod2.reverse_it(n))

m = int(input('Введите число m: '))
print(mod2.count_first(m))

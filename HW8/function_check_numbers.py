def fun_check(num, *args):
    num_list = args
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            if i != j and num_list[i] + num_list[j] == num:
                return True
    return False


lst1 = [i for i in range(0, 12)]

print(lst1)
print(fun_check(33, *lst1))
print(fun_check(11, *lst1))

lst2 = [i for i in range(0, 75, 7)]

print(lst2)
print(fun_check(20, *lst2))
print(fun_check(35, *lst2))
def check_num(num):
    if num == 1:
        return False

    count = 0

    for x in range(2, num):
        if num % x == 0:
            count += 1

    if count >= 1:
        return False
    else:
        return True


def fun_nums_gen(num=1):
    while True:
        if check_num(num): yield num
        num += 1


max_num = 100

print(f'Список простых чисел от 1 до {max_num}: ', end='')

for n in fun_nums_gen():
    if n > max_num: break
    print(n, end=' ')
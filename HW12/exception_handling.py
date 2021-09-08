def exception():
    a = input("Введите 1 значение: ")
    b = input("Введите 2 значение: ")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        con = ''.join(map(str, (a, b)))
        # seq = (a, b)
        # con = ''.join(seq)
        print("Соединение строк: ", con)
    else:
        s = a + b
        print("Сумма чисел: ", s)


exception()

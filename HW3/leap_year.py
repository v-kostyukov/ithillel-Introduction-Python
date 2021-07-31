year = int(input("Введите год: "))

if type(year) == int and 1900 < year < 1000000:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is leap year")
            else:
                print(year, "is not leap year")
        else:
            print(year, "is leap year")
    else:
        print(year, "is not leap year")
else:
    print("Вы неправильно указали год! Введите год в диапазоне с 1900 до 1000000")

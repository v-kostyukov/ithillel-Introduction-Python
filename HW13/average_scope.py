# f = open('src_14.txt', 'r', encoding='UTF-8')
# data = f.read()
# f.close()
pupils = {}
with open('src_14.txt', 'r', encoding='UTF-8') as data:

    for line in data.readlines():
        f_name, l_name, *lst = line.split()
        # print(line)

        full_name = ' '.join([l_name, (f_name[0] + '.')])

        s = 0
        count = 0

        for i in lst:
            s = int(i)
            count += 1

        pupils[f_name] = round(s / count, 2)

average = 0
count = 0

for k in pupils.keys():
    average += pupils[k]
    count += 1

    if pupils[k] < 5:
        print("{:25s} {:.2f}".format(k, pupils[k]))

#
# inform = inform.split("\n")
# pupils = []
#
# for line in inform:
#     line = line.split(" ")
#     pupils.append((line[0], line[1], line[2]))
#     print(pupils)

# average = 0
#
# print("Ниже 3 баллов:")

# for p in pupils:
#     average += int(p[2])
#     if p[2] < 3:
#         print(f"{p[0]} {p[1]}: {p[2]}")
#         average /= len(pupils)
# print(f"Средняя оценка по классу: {average}")

#    g = int(line[len(line)-2])
#    s += g
#    n +=1
#    if g < 5:
#        print(i[:-1])
# print('Средний балл: %.2f' % (s/n))

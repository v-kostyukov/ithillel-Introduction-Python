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

print('{:25s} {:5s}'.format('Средний балл по группе :',
                                str(round(average / count, 2))))

with open('src_1.txt', 'w', encoding='utf-8') as out_file:
    for k in pupils.keys():
        line = '{:25s} {:.2f}{:1s}'.format(k, pupils[k], '\n')
        out_file.write(line)
file_name = input("Создаем файл: ")
f = open(file_name, 'w')

while True:
    s = input("Введите данные: ")
    if s == '': break
    f.write(s+'\n')
f.close()

fid = open(file_name, 'r')
print(fid.readlines())

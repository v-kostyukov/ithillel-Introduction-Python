a = [45, 34, 23, 12, 56, 11, 8, 2]                  # Список a

k, C = [3, 77]                                      # Множественное присваивание, справа от "=" стоит список из двух элементов, а слева две переменные

a.append(0)                                         # Добавляем элемент используя метод append
for i in range(len(a) - 1, k, -1):                  # Цикл пробегаемся в диапазоне
    a[i] = a[i - 1]                                 # Делаем сдвиг
a[k] = C                                            # Делаем вставку уже в считанном списке
print(' '.join([str(i) for i in a]))                # Преобразование списка в строку методом join
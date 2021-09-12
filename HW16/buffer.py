from random import randint


class Buffer:
    def __init__(self):
        self.elements = list()
        self.sum_elements = 0

    def add(self, *a):
        for number in a:
            self.elements.append(number)

            if len(self.elements) == 5:
                for element in self.elements:
                    self.sum_elements += element
                self.elements.clear()
                print(f"Сумма 5 элементов: {self.sum_elements}")
                self.sum_elements = 0

    def get_current_part(self):

        return self.elements


buffer = Buffer()

for i in range(10):
    elements = [randint(0, 10) for j in range(randint(1, 20))]
    print(f"Генерация чисел: {elements}")
    buffer.add(*elements)
    print(f"Текущая часть в буфере: {buffer.get_current_part()}")

class DigitalCounter:
    counter = 0

    def __init__(self, min_v, max_v):
        self.counter = min_v
        self.maximum = max_v

    def overflow(self):
        if self.counter < self.maximum:
            self.counter += 1
        return self.counter

    def status(self):

        return self.counter


c = DigitalCounter(3, 5)
print("Текущее состояние счетчика: ", c.status())
print(c.overflow())
print(c.overflow())
print(c.overflow())

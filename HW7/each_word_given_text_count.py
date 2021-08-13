s = "На дворе трава раз трава два дрова не руби дрова три трава и дрова"
counter = {}
for word in s.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
    print(counter)
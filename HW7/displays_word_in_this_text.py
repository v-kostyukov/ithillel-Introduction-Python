from string import punctuation

text = input("Введите текст: ").lower().split()
num = {}

for i in text:
   if i in punctuation:
           i = i.replace(punctuation,"")
   try:
       num[i] += 1
   except:
       num[i] = 1
word = max(num)
for i in num:
   if num[i] >= num[word]:
       word = i

print(word)
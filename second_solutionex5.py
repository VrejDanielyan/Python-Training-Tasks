# text = input('Enter your text: ')
# print(text.count('a'))

text = input('Enter your text: ')
latter = input('Enter your latter: ')
c = 0
for i in text:
    if i == latter:
        c = c + 1
print(c)
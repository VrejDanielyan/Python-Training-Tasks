'''Implement lambda function to calculate power of the given input number,
assign the funciton to variable and apply on given user input,
print result: e.g. inputs are 3, 5, 9'''
ls = [3, 5, 9]

#1
import math

for i in ls:
    print(f'#1: {int(math.pow(i, 2))}')

#2
for j in ls:
    res = lambda a: a ** 2
    print(f'#2: {res(j)}')

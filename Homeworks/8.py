'''Generate positive random number between 2 numbers got from command line args and check if that number is պարզ.
Program should print X number is simple or X number is NOT simple
'''
import random

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
n = random.randint(first_number, second_number)

print(n)

for i in range(first_number, second_number):
    count = 0
    divider = 2
    print(i)
'''8. Generate positive random number between 2 numbers got
from command line args and check if that number is պարզ.
Program should print X number is simple or X number is NOT simple'''
import random
import sys


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num = random.randint(num1, num2)

print(num)
for i in range(2, num):
    if (num % i) == 0:
        print(f'{num} is not a prime')
        break
else:
    print(f'{num} is a prime')

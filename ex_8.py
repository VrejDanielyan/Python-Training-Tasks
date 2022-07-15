# Generate positive random number between 2 numbers got from command line args and check if that number is պարզ.
# Program should print X number is simple or X number is NOT simple



import sys
import random
import math


y = random.randint(int(sys.argv[1]), int(sys.argv[2]))
x = round(math.sqrt(y))
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    if(x != 0):
        print(y, 'is prime')
    else:
        print("1 is not prime")
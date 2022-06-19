#Generate positive random number between 2 numbers got from command line args
# and check if that number is պարզ.
# Program should print X number is simple or X number is NOT simple

import sys
import random

a = int(sys.argv[1])
b = int(sys.argv[2])
n = random.randint(a, b)

if n > 2:
 for i in range(2, n//2):
    if (n % i) == 0:
       print(n, "is not a prime number")
       break
    else:
       print(n, "is a prime number")
else:
  print(n, "is neither prime nor composite")

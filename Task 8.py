import sys
import random
a = int(sys.argv[1])
b = int(sys.argv[2])
if a < 0:
    n = random.randint(0, b)
else:
    n = random.randint(a, b)
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

import sys
import random
i = int(sys.argv[1])
j = int(sys.argv[2])
n = random.randint(i, j)
for number in range(2, n):
    if (n % number) == 0:
        print(n, "is not a parz")
        break
else:
    print(n, "is a parz")


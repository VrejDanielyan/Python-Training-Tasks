#Implement function which will print numbers from 1 to N
# where N is given number to function argument -
# function should not contain loop construction.

'''n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(i, end = ' ')'''


def number(n):
  if n > 0:
    number(n - 1)
    print(n, end = ' ')

n = int(input("Number is: "))
number(n)

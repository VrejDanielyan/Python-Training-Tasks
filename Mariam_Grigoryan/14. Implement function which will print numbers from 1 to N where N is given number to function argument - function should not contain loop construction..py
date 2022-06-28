# 14. Implement function which will print numbers from 1 to N where N is given number to function argument - function should not contain loop construction.

def numbers(n):
    if n>0:
        (numbers(n-1))
        print(n, end=' ')

numbers(5)
# 14. Implement function which will print numbers from 1 to N where N is given number to function argument - function should not contain loop construction.

def number(n):
    if n == 0:
        return
    else:
        number(n - 1)
        print(n)

(number(15))

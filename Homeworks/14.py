'''Implement function which will print numbers from 1 to N where N is
given number to function argument - function should not contain loop construction.'''


def num_n(n):
    if n > 0:
        num_n(n - 1)
        print(n)

num_n(10)

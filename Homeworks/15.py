'''Implement function which will return fibonacci Nth number - N is function argument '''
'''0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...'''

def fib(n):
    if n < 0:
        print('aaaaa')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))

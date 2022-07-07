#15. Implement function which will return fibonacci Nth number-
#N is function argument

def fib(n):
    if n <= 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Input a number to get the fibonacci: "))
print(fib(n))
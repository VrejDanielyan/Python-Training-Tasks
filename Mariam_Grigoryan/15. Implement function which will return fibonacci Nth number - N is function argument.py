# 15. Implement function which will return fibonacci Nth number - N is function argument

def fibonacci(n):
    if n<=1:
        return n

    else:
        return (fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(5))

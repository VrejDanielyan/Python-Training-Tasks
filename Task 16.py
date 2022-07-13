# 16. Implement function which will return factorial of  given N number - N is function argument

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(7))

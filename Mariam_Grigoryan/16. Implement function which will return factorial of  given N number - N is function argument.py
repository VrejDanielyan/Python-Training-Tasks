# 16. Implement function which will return factorial of given N number - N is function argument

def factorial(n):
    if n==1:
        return 1

    else:
        return n*factorial(n-1)

print(factorial(5))

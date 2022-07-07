#16. Implement function which will return factorial of  given N number -
# N is function argument

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Input a number to get the factiorial : "))
print(factorial(n))
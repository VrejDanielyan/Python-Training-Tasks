'''Implement function which will return factorial of given N number - N is function argument '''

def fact(x):
    if x == 1:
        return 1
    return fact(x-1) * x

print(fact(5))
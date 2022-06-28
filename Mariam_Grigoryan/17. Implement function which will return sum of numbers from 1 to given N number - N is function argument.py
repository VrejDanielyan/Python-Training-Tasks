# 17. Implement function which will return sum of numbers from 1 to given N number - N is function argument

def gumar(n):
    if n==0:
        return 0

    else:
        return n+ gumar(n-1)

print(gumar(6))
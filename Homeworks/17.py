'''Implement function which will return sum of numbers from 1 to given N number - N is function argument '''

def sumnum(n):
    for i in range (1, n):
        if n < i:
            break
        else:
            return sumnum(n) + sumnum(n+1)

sumnum(15)

#1+2+3+4+5+6
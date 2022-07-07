# 17.Implement function which will return sum of numbers
#from 1 to given N number -N is function argument

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)

n = int(input("Enter the number: "))
print(sum(n))
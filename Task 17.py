# 17. Implement function which will return sum of numbers from 1 to given N number - N is function argument
def amount(n):
    if n == 1:
        return 1
    else:
        return amount(n - 1) + n

print(amount(9))

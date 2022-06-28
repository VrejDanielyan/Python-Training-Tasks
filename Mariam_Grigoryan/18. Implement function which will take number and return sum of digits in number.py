# 18. Implement function which will take number and return sum of digits in number

def sum_digits(n):
    if n//10 < 1:
        return n

    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(1235))

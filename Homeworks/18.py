'''Implement function which will take number and return sum of digits in number '''

def sum(num):
    result = 0
    for i in num:
        result = result + int(i)

    return result


num = "12"
print(sum(num))
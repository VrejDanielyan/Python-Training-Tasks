'''Implement function to return ամենամեծ ընդհանուր բաժանարար '''

a = 15
b = 25

def amena(a, b):
    if a < b:
        minimum = a
    else:
        minimum = b
    for i in range(minimum, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(amena(a,b))
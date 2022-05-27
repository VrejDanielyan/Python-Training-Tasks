from random import randint
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
if number1 < number2:
    value = randint(number1, number2)
else:
    value = randint(number2, number1)
def isprime(value):
    for n in range(2,int(value*0.5)+1):
        if value%n==0:
            return f"{value} is NOT simple"
    return f"{value} is simple"
print(isprime(value))





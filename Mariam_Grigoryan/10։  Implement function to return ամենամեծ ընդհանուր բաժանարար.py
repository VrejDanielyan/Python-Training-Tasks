number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
a = []
try:
    for i in range (2, number1):
        for j in range (2, number2):
            i=j
            if number1%i == 0 and number2%j ==0:
                a.append(i)
        break
    print(a[-1])
except IndexError:
    print("No divisors")
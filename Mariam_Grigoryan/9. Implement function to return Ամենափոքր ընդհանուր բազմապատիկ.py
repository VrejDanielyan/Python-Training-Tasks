def divisors(number1, number2):
   if number1 > number2:
       greater = number1
   else:
       greater = number2

   while True:
       if greater % number1 == 0 and greater % number2 == 0:
           divisor = greater
           break
       greater += 1

   return divisor

number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))

print(f"The divisor is {divisors(number1, number2)}")
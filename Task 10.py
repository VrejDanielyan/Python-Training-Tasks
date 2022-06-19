# Implement function to return ամենամեծ ընդհանուր բաժանարար

def compute_GCD(first_number, second_number):
   if second_number == 0:
       return first_number
   else:
       return compute_GCD(second_number, first_number%second_number)
    
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
print("Greatest Common Divisor is:", compute_GCD(first_number, second_number))

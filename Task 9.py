# Implement function to return Ամենափոքր ընդհանուր բազմապատիկ


def compute_LCM(first_number, second_number):
   if first_number > second_number:
       greater = first_number
   else:
       greater = second_number
   value = greater
   while(True):
       if((greater % first_number == 0) and (greater % second_number == 0)):
           print("LCM is:", greater)
           break
       greater += value
first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
compute_LCM(first_number, second_number)

# Implement lambda function to calculate power of the given input number,
# assign the funciton to variable and apply on given user input, print result: e.g. inputs are 3, 5, 9


number = int(input("Enter any number: "))
power = int(input("Enter Power: "))
result = lambda number: number**power
print(result(number))

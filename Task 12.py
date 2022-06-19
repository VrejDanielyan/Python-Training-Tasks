# Implement lambda function to return ""Full name: <name> - <surname>"" string, taking name and surname from args,  assign to variable and apply on given user inputs, print result

name = input("Enter your name: ")
surname = input("Enter your surname: ")
full_name = lambda name,surname: f"Full name: {name}-{surname}"
print(full_name(name,surname))

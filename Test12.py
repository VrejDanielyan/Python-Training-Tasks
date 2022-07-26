#Implement lambda function to return ""Full name: <name> - <surname>"" string,
# taking name and surname from args,  assign to variable and apply on given user inputs,
# print result

first_name = input("First name: ")
last_name = input("Last name: ")
full_name = lambda first_name, last_name: f"{first_name} - {last_name}"
print(full_name(first_name, last_name))

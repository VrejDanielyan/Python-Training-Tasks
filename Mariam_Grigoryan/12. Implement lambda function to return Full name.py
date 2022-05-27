fname = input("First name: ")
surname = input("Last name: ")
name = lambda fname, surname: f"{fname} - {surname}"
print(name(fname, surname))
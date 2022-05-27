x = '*'
y = 1
z = int(input("Enter a number: "))
if z > 0:
    while y <= z:
        print(x * y)
        y += 1
else:
    print("Pleas enter a positive number")

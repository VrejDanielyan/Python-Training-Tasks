rows = int(input("Enter a number:  "))
for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for j in range(rows, i, -1):
        print("*", end="")
    print()

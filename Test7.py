n = 5
for i in range(n):
    for j in range(n - i - 1): # loop for space
        print(" ", end = "")
    for j in range(i + 1):    # loop for star
        print("*", end = " ")
    print()
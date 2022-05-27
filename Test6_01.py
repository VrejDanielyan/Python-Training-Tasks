left_triangle = int(input("Number of rows: "))
for i in range(left_triangle):
    for j in range(i + 1):
        print("*", end = "")
    print()
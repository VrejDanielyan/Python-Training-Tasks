# for i in range(output, 0, -1):
#     for j in range(output):
#         print(j * " ", end="")
#         print((i-j)*"*")
#     break


output = int(input("Enter your number: "))
for j in range(output):
    print(j * " ", end="")
    print((output-j)*"*")

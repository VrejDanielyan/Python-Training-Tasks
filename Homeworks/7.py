'''Python code to print triangle with fixed size
*****
 ****
  ***
   **
    *'''

sim_count = int(input('Please enter any number: '))
space = 2 * sim_count - 2

for i in range(0, sim_count):
    for j in range(0, space):
        print(end=" ")

    space = space - 2

    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")



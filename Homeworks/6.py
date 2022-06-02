''' Python code to print triangle with fixed size
*
**
***
****
*****'''

# Without list and list methods
sim_count = int(input('Please enter any number: '))

for i in range(sim_count):
    print('*' * i)

# With list and list methods

sim_list = []
for i in range(1, sim_count + 1):
    sim_list.append("*" * i)
    print(sim_list)
print("\n".join(sim_list))
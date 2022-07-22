# Iterate list of numbers and print only Odd numbers with list comprehension
def only_odd(entire_list):
    return [i for i in entire_list if i % 2 == 1]


print(only_odd([1, 12, 43, 54, 26, 94, 33, 86, 49, 55, 9]))


# One line
print([i for i in [1, 12, 43, 54, 26, 94, 33, 86, 49, 55, 9] if i%2==1])

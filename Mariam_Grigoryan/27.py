#  Iterate list of numbers and print "Odd" if number is Odd else "Even" if number is Even with list comprehension
def odd_or_even(list):
    return ["Odd" if i % 2 == 1 else "Even" for i in list]


print(odd_or_even([1, 2, 2, 3, 5, 34, 65, 76, 45, 33, 53]))
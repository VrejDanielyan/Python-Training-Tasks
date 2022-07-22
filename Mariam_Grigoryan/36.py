# Write a Python program to find
# the key of the maximum value in a dictionary



def value_of_maximum_key():
    d = {55: "a", 23: "b", 78: "c", 12: "d"}
    list_of_keys = [key for key in d]
    max_key = max(list_of_keys)
    for key in d:
        if key == max_key:
            return d[key]

print(value_of_maximum_key())

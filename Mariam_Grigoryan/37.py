# Write a function which will return dict key of maximum value.
def key_of_max_value():
    d = {'a':7, 'b': 9, 'c':-2}
    list_of_values = [d[key] for key in d]
    max_value = max(list_of_values)
    for key in d:
        if d[key] == max_value:
            return key

print(key_of_max_value())

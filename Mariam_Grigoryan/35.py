# Write a Python program to combines two or more dictionaries, creating a list of values for each key.
def list_of_values():
    d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
    d2 = {'x': 300, 'y': 'Red', 'z': 600}
    d3 = {}

    for key in d1:
        if key in d2:
            d3[key] = [d1[key], d2[key]]

        elif key not in d1:
            d3[key] = [d2[key]]

        elif key not in d2:
            d3[key] = [d1[key]]

    return d3

print(list_of_values())

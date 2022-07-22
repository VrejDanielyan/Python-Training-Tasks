# Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
from collections import Counter
d3 = Counter(d1) + Counter(d2)
print(d3)


# Without external library
def common_keys():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    d3 = {}

    for key in d1:
        if key in d2:
            d3[key] = d1[key] + d2[key]
        else:
            d3[key] = d1[key]

    for key in d2:
        if key not in d1:
            d3[key] = d2[key]

    return d3

print(common_keys())

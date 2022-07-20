# Write a Python script to concatenate dictionaries to create a new one
def concatenate_dict():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    concatenated_dict = {}

    for i in (dic1, dic2, dic3):
        concatenated_dict.update(i)
    return concatenated_dict

print(concatenate_dict())

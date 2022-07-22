# Write a Python script to check whether a given key already exists in a dictionary.
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def key_exist(key):

    if key in dic:
        return True

    else:
        return False


print(key_exist(4))
print(key_exist(50))

# One line
print(True if 50 in {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} else False)

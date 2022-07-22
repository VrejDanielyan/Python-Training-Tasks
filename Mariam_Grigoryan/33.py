# Write a function which will take string and return dictionary with letters
# and count of letters in a string as a value of keys
def count_letters(text):
    dic = {}

    for letter in text.lower():
        if letter in dic.keys():
            dic[letter] += 1

        else:
            dic[letter] = 1

    return dic

print(count_letters("Mariam Grigoryan"))

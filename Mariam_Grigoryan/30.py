# Write a program which will create e dictionary with 1-15 numbers as a key and values are square of keys
def dic_with_squares():
    squares = dict()
    for i in range(1, 16):
        squares[i] = i ** 2
    return squares


print(dic_with_squares())

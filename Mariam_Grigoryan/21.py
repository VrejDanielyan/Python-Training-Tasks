#  Function to return binary representation of decimal number
def decimal_to_binary(decimal):
    binary = ''
    if decimal == 0:
        return ''
    elif decimal < 0:
        return "Please enter a postive integer"
    else:
        return str(decimal_to_binary(decimal // 2)) + str(decimal % 2)


print(decimal_to_binary(13))
print(decimal_to_binary(9))
print(decimal_to_binary(20))
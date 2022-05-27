number = int(input('Enter a number: '))
letter = input('Enter a letter: ')
if number > 0 and len(letter) == 1:
    x = number * letter
    print(x)
elif number <= 0:
    print("Please enter a positive number")
elif len(letter) != 1:
    print("Please enter only one letter")
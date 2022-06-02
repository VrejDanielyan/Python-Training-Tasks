'''Get 2 user inputs: 1-number, 2-letter -> print number amount of letters in one line:
e.g. user inputs are 3 and 'a', output should be 'aaa'''

simbol = input('Please enter any simbol: ')
count = input('Enter any number: ')

print(f'{simbol} * {count} = {simbol * int(count)}')
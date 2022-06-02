'''Function to check is given number polindrom '''


inputString = input('input string: ')

def solution(inputString):
    rev = inputString[::-1]
    if rev == inputString:
        print(f'{inputString} and {inputString[::-1]}')
        return True
    else:
        print(f'{inputString} and {inputString[::-1]}')
        return False

print(solution(inputString))
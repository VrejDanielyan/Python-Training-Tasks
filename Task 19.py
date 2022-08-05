# 19. Function to check is given number palindrome

def check_palindrome(n):
    if len(n) < 1:
        return True
    else:
        if n[0] == n[-1]:
            return check_palindrome(n[1:-1])
        else:
            return False
num = input(("Enter a number: "))
if(check_palindrome(num)):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

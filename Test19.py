def check_palindrome(s):
    # Base Case
    if len(s) <= 1:
        return True

    # Recursive Case
    if s[0] == s[len(s) - 1]:
        return check_palindrome(s[1:len(s) - 1])
    else:
        return False


if (check_palindrome(str(123421))):  # Converting the number to string
    print("Palindrome")
else:
    print("Not a Palindrome")
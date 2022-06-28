#19. Function to check is given number polindrom

def palindrome(m):
    m=str(m)
    if len(m) <= 1:
        return True

    if m[0] == m[len(m) - 1]:
        return palindrome(m[1:len(m) - 1])
    else:
        return False

print(palindrome('step on no pets'))
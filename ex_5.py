# Get user input: string - calculate and print amount of ""a"" letters in a string
#(2 solutions, one using python's string method, other one implament your own algorithm for that)

# any_word = input("Please enter: ")
# print ("In your word the count of letter 'a' is", any_word.count('a'))

count = 0
any_word = input("Please enter: ")
letter = "a"
for i in any_word:
    if i == letter:
        count += 1
print(count)
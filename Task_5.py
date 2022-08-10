# Get user input: string - calculate and print amount of "a" letters in a string (2 solutions, one using python's string method, other one implament your own algorithm for that)
# e.g. user input is 'ararat', output will be 3

# 1st solution:
word = input ("Enter your text: ")
i = word.count("a")+word.count("A")
print(i)

# 2nd solution:

word = input ("Enter your text: ")
n=0
for letter in word:
    if letter == "A" or letter == "a":
        n+=1

print (n)











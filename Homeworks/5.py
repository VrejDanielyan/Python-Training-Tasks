'''Get user input: string - calculate and print amount of "a" letters in a string
e.g. user input is 'ararat', output will be 3'''

word = input('Enter any word: ').upper()

# print(word.count('a'))

def calc_char(word):
    find_sim = input('Enter find simbol: ')
    sim_count = 0
    for char in word:
        if char == find_sim:
            sim_count += 1
            print(f'{find_sim} and {sim_count}')
    print(sim_count)

calc_char(word)


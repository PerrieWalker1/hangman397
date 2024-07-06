import random

word_list = ['apple', 'banana', 'strawberry', 'orange', 'lemon']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Enter a single letter: ')

# if guess valid print('Good guess!')
if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
else:
    print('Oops! That is not a valid input.')
    

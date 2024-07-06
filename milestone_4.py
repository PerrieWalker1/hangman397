import random

word_list = ['red', 'one', 'end']

class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_letters = self.word_guessed.count('_')
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for ind, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[ind] = guess
                    self.num_letters -= 1
                    print(self.num_letters)

               

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if len(guess) > 1 or guess.isalpha() is False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

                
        

        



game = Hangman(word_list)

# print(game.word)
# print(game.word_guessed)
# print(game.num_letters)
game.ask_for_input()
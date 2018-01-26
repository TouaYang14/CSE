import random


# Hangman
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 3. Add a guess to the list of letters guessed
# 4. Reveal letters based on input
# 5. Create win and lose conditions

import string

letters_guessed = []

guesses = 10

print("Welcome to Hangman!!")

words_bank = ["nani", "edison", "georgie", "exit", "tree", "clock", "hood", "whale", "turtle", "batman"]

random_word = random.choice(words_bank)

letters = list(string.ascii_lowercase)

print(random_word)

while guesses > 0:
    guesses -= 1
    print("These are your letters %s" % letters_guessed)
    answers = input("Guess a letter ")

    lower = answers.lower()
    letters_guessed.append(lower)
    print("You have %s guesses left" % guesses)
    if letters == random_word:
        print("You win!")

print("Game Over")

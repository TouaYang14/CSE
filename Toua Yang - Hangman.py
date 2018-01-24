import random

import string

letters_guessed = []

guesses = 10

print("Welcome to Hangman!!")

words_bank = ["NANI", "EDISON", "Georgie", "EXIT", "TREE", "TOUA", "HOOD", "WHALE", "EZIO", "BATMAN"]

random_word = random.choice(words_bank)

print(random_word)




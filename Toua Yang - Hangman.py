import random

import string

print("Welcome to Hangman")

words_bank = ["NANI", "GTX_1080_TI", "Georgie", "EXIT", "TREE", "TOUA", "HOOD", "WHALE", "EZIO", "HASAKEY"]

brain = random.choice(words_bank)

print("you have to guess the word")
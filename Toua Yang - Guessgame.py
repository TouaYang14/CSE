# Toua Yang

import random
random_number = (random.randint(1, 50))

guesses = 5

number = input("What number do you think I am thinking of? ")


if str(random_number) == number:
    print("You win")

if str(random_number)!= number:

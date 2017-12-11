# Toua Yang

import random
random_number = (random.randint(1, 50))

guesses = 5

number = -1
while str(random_number) != number and guesses > 0:
    number = input("What number do you think I am thinking of? ")

    if str(random_number) == number:
        print("You win")

    if str(random_number) != number:
        guesses -= 1

    if number < str(random_number) and guesses > 0:
        print("Guess Higher")
        print("Guess again")
        print("You have %s guesses left." % guesses)

    if number > str(random_number) and guesses > 0:
        print("Guess Lower")
        print("Guess again")
        print("You have %s guesses left." % guesses)

if guesses == 0:
    print("You lose")

print("You have %s guesses left." % guesses)

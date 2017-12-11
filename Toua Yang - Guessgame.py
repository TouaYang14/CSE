# Toua Yang

import random
random_number = (random.randint(1, 50))

guesses = 4

number = -1
while str(random_number) != number and guesses > 0:
    number = input("What number do you think I am thinking of? ")

    if str(random_number) == number:
        print("You win")

<<<<<<< HEAD
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
=======

if str(random_number) == number:
    print("You win")

 elif int(guesses) <= random_number:
    print("Guess Lower")


if str(random_number)!= number:
    guesses -= 1
    number = input("Take another guess ( ͡° ͜ʖ ͡°)...")


elif int(guesses) <= random_number:
    print("Guess Lower")

if str(random_number)!= number:
    guesses -= 1
    number = input("Take another guess ( ͡° ͜ʖ ͡°)...")

elif int(guesses) <= random_number:
    print("Guess Lower")


if str(random_number)!= number:
    guesses -= 1
    number = input("Take another guess ( ͡° ͜ʖ ͡°)...")


elif int(guesses) <= random_number:
    print("Guess Lower")


if str(random_number)!= number:
    guesses -= 1
    number = input("Take another guess ( ͡° ͜ʖ ͡°)...")


elif int(guesses) <= random_number:
    print("Guess Lower")


if guesses == 0:
    print("You lose")
>>>>>>> 97f051000f409f8b4b87f38617d7d30361058877

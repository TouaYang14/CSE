# Toua Yang

import random
random_number = (random.randint(1, 50))

guesses = 4

number = input("What number do you think I am thinking of? ")



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
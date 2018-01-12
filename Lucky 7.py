import random

money = 15

most_money = 0

total_rounds = 0

rounds = 0

while money > 0:
    r1 = random.randint(1, 6)

    r2 = random.randint(1, 6)

    if (r1 + r2) != 7:
        money = money - 1
        rounds += 1
        print("You lost the bet. You lost a dollar.")
        print("You now have $%s." % money)

    if (r1 + r2) == 7:
        money = money + 4
        rounds += 1
        print("You won the bet, you got 5 dollars")
        print("You now have $%s." % money)

    if money > most_money:
        most_money = money
        total_rounds = rounds


print("You did %s rounds." % rounds)

print("Your money is %s dollars." % money)

print("Your high score was %s rounds" % highest_round)

print("Game Over")
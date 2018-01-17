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

print("You now have %s dollars." % money)

print("You should've stopped at round %s when you had $%s dollars" % (total_rounds, most_money))

print("Game Over")

import random

money = 15

rounds = 0

while money > 0:
    r1 = random.randint(1, 6)

    r2 = random.randint(1, 6)

    if (r1 + r2) != 7:
        money = money - 1
        rounds += 1
        print("You lost the bet. You lost a dollar.")
        print("You know have $%s." % money)

    if (r1 + r2) == 7:
        money = money + 4
        rounds += 1

print("You did %s rounds." % rounds)

print("Your Money is %s dollars." % money)

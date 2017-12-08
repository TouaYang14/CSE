def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name + " " + first_name))  # concatenation


def reverse_order():
    first_name = input("First name")
    last_name = input("Last name")
    print("%s, %s" % (last_name, first_name))


# 12/5/17


def add_py(name):
    print("%s.py" % name)  # Solution 1
    print(name + ".py")  # Solution 2


# 12/6/17


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(90, 900, 9000)


def repeat(num1):
    print("%s" % num1)
    print("%s" % num1)
    print("%s" % num1)


# 12/8/17


def date(month, day, year):
    print(month + "/" +  day + "/" + year)

date("12", "8", "17")
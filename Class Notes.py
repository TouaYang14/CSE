# Defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand): # TWO underscores before and after
        # Things a shoe has
        self.lace_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean = False
        print("You wear the shoes")

    def wash(self):
        self.clean = True
        print("You clean the shoes")


first_pair = Shoes("Red", True, "Jordan")
second_pair = Shoes("Pink", False, "Sketchers")

print(first_pair.brand)
print(second_pair.lace_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)
first_pair.wash()
print(first_pair.clean)


class Cars(object):
    def __init__(self, tires, horsepower, color, pice, model):
        self.Tires = Tires
        self.hp = horsepower
        self.color = White
        self.price = 3,400,000
        self.model = Lykan_Hypersport

    def drive_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
            print("You start the car")
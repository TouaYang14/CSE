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
    def __init__(self, tires, horsepower, White, Three_Million, Lykan_Hypersport):
        self.Tires = tires
        self.hp = horsepower
        self.color = White
        self.price = Three_Million
        self.model = Lykan_Hypersport
        self.passengers = 0
        self.running = False

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

    def turn_off(self):
        if self.running:
            self.running = False
            print("You have turned off the car")
        else:
            print("Nothing Happens")

    def go_for_drive(self, passengers):
        print("%d passengers get in" % passengers)
        self.passengers = passengers
        self.turn_on()
        self.drive_forward()
        self.drive_forward()
        self.drive_forward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passengers = 0


my_car = Cars("Red", "Tesla", "X", 9001, "w")
my_car.go_for_drive(4)

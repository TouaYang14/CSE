# import statements
# class definitions
# items
# characters
# rooms
# instantiate classes
# controller


class Item(object):
    def __init__(self, description, name):
        self.equip = False
        self.unequip = True
        self.description = description
        self.name = name

    def use(self):
        print("You used the item")


class Weapons(Item):
    def __init__(self, attack, block, name, description):
        super(Weapons, self).__init__('Tools that you use to do damage', 'Weapons')
        self.equip = False
        self.unequip = True
        self.attack = attack
        self.block = block
        self.name = name
        self.description = description


class WoodenSword(Weapons):
    def __init__(self):
        super(WoodenSword, self).__init__(57, 0, 'wooden_sword', 'a wooden sword')


class Shield(Weapons):
    def __init__(self):
        super(Shield, self).__init__(0, 50, 'wooden_shield', 'An old rusty shield')


class BattleAxe(Weapons):
    def __init__(self):
        super(BattleAxe, self).__init__(90, 30, 'Battle_Axe', 'A Battle Axe')


class Wings(Item):
    def __init__(self):
        super(Wings, self).__init__('Wings, that can make you fly', 'Wings')


class Clock(Item):
    def __init__(self):
        super(Clock, self).__init__('A clock that can tell you what time it is', 'Clock')


class Compass(Item):
    def __init__(self):
        super(Compass, self).__init__(' A compass that tells you where North, East, West, and South is', 'Compass')


class Equipment(Item):
    def __init__(self, name, description, value):
        super(Equipment, self).__init__('Something that you wear', 'Equipment')
        self.equip = False
        self.unequip = True
        self.name = name
        self.description = description
        self.value = value


class Armor(Equipment):
    def __init__(self):
        super(Armor, self).__init__('Armor for the chest', 'Chestplate, where\n'
                                                                    ' only those who have enough potential can use it',
                                                                    500)


class BootsOfSwiftness(Equipment):
    def __init__(self):
        super(BootsOfSwiftness, self).__init__('BootsOfSwiftness', 'a boot that makes you go faster', 500)


class PitKey(Item):
    def __init__(self):
        super(PitKey, self).__init__('The key that is require to open the door in pit at long', 'PitKey')


class Gauntlet(Equipment):
    def __init__(self):
        super(Gauntlet, self).__init__('Gauntlet', 'A gauntlet that is used to wield some objects', 400)


class SteelSword(Weapons):
    def __init__(self):
        super(SteelSword, self).__init__(68, 0, 'Steel Sword', 'A sturdy steel sword')


class SteelShield(Weapons):
    def __init__(self):
        super(SteelShield, self).__init__(100, 600, 'Steel Shield', 'A steel\n'
                                                                    ' shield that is better than the wooden shield')


class Character(object):
    def __init__(self, name, health, armor, description, dialogue):
        self.name = name
        self.inventory = []
        self.health = health
        self.armor = armor
        self.description = description
        self.dialogue = dialogue
    def heal(self):
        if self.health <= 5:
            self.health += 25



wooden_sword = WoodenSword()
shield = Shield()
battle_axe = BattleAxe()
wings = Wings()
clock = Clock()
compass = Compass()
armor = Armor()
bootsofswiftness = BootsOfSwiftness()
pitkey = PitKey()
gauntlet = Gauntlet()
steelsword = SteelSword()
steelshield = SteelShield()


Snapper = Character('Snapper', None, 320, 0, "Snapper is a turtle , that is seeking to Ionia\n"
                    " so he can deliver a message to the Master", None)

Villager1 = Character('Tom', None, 200, 0, 'A villager that is wondering around the town.', None)


class Room(object):
    def __init__(self, name, north, south, east, west, items, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Intialize Rooms
noxus = Room('noxus', 'top_mid', None, 'outsideoflongdoors', 'outsideoftunnels', None, 'You are in Noxus, you must\n'
                                                                                       ' find a way to get to Ionia')
outsideoftunnels = Room('outsideoftunnels', 'tunnels', 'noxus', None, None, wooden_sword, 'You are outside of Tunnels')
outsideoflongdoors = Room('outsideoflongdoors', 'longdoors', 'noxus', None, 'top_mid', None, 'You are outside\n'
                          ' of Long Doors')
longdoors = Room('longdoors', None, 'outsideoflongdoors', 'long', None, armor, 'You are in\n'
                 ' Long Doors, you see 5 boxes on top of each other')
long = Room('long', 'icathia', None, None, 'longdoors', None, 'You are at Long, you see a mist of\n'
            ' clouds north.')
tunnels = Room('tunnels', 'howling_marsh', 'outsideoftunnels', 'lower_tunnels', None, battle_axe, 'You are inside\n'
               ' of Tunnels, and you see an axe, you see a staircase leading down from the\n'
               ' east, and light from the north')
lower_tunnels = Room('lower_tunnels', None, None, 'mid', 'tunnels', [clock, compass], 'You are in lower\n'
                     ' tunnels, you see a clock and a compass on the table')
mid = Room('mid', 'mid_doors', 'top_mid', 'staircase', 'lower_tunnels', None, 'You are at mid and you see a\n'
           'door to the west and a door to the north.')
pit = Room('pit', 'long', 'pitdoor', 'longdoors', None, None, 'The pit.. There is a door to the south')
pitdoor = Room('pitdoor', 'pit', None, None, None, wings, 'Where the wings lies. You see the wing on the ground')
staircase = Room('staircase', 'shadow_isle', 'top_mid', None, 'mid', None, 'You see a hallway\n'
                 ' turning right, and it is\n'
               ' leading to a stair case, with dark and misty clouds. As your feet tremble you hear a sound.')
shadow_isle = Room('shadow_isle', None, 'staircase', 'icathia', None, gauntlet, 'You\n'
                   ' are finally in the Shadow Isle and there are thick clouds. You feel\n'
                   ' as if someone is watching you, and you see a steel shield laying on the ground.')
icathia = Room('icathia', 'goose', 'long', None, 'shadow_isle', bootsofswiftness, 'You are in Icathia, this City\n'
               ' is close to Ionia')
ionia = Room('ionia', None, None, None, 'mid_doors', None, 'You have finally reached Ionia, and people\n'
             'welcome you to the City.')
goose = Room('goose', None, 'icathia', None, None, steelsword, 'You are in the ally\n'
             ' of goose, it is a small ally wih a small, you see a shield lying on the ground.')
howling_marsh = Room('howling_marsh', None, 'tunnels', 'mid_doors', None, steelshield, 'You are in Howling\n'
                     ' Marsh.... You feel as very unsafe and see dead trees everywhere.')
top_mid = Room('top_mid', 'mid', 'noxus', 'outsideoflongdoors', None, None, "You\n'"
               "are at the top of mid. You don't see\n"
               " anything particular that is interesting at all. You see a ramp going down to the north.")
mid_doors = Room('mid_doors', None, 'mid', 'ionia', 'howling_marsh', None,'You are at mid doors, and to your west you\n'
                 ' see a shadowing place, and to your right is ionia.')


current_node = noxus
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']

while True:
    if Item in current_node is not None:
        print("Do you want pick up the item bro?")
        print(Item.name)
    if command == ('take %s' % Item.name)
        Item.append.inventory
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        # Look for which command we typed in
        pos = short_direction.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not Recognized")
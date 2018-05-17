# import statements
# class definitions
# items
# characters
# rooms
# instantiate classes
# controller


class Item(object):
    def __init__(self, name, description):
        self.equip = False
        self.unequip = True
        self.name = name
        self.description = description


class Weapons(Item):
    def __init__(self, attack, block, name, description):
        super(Weapons, self).__init__('Tools that you use to do damage', 'Weapons')
        self.equip = False
        self.unequip = True
        self.attack = attack
        self.block = block
        self.name = name
        self.description = description


class Dagger(Weapons):
    def __init__(self, attack, block, name, description):
        super(Dagger, self).__init__(attack, block, name, description)


class WoodenSword(Weapons):
    def __init__(self, attack, block, name, description):
        super(WoodenSword, self).__init__(attack, block, name, description)


class Shield(Weapons):
    def __init__(self, attack, block, name, description):
        super(Shield, self).__init__(attack, block, name, description)


class BattleAxe(Weapons):
    def __init__(self, attack, block, name, description):
        super(BattleAxe, self).__init__(attack, block, name, description)


class Wings(Item):
    def __init__(self, name, description):
        super(Wings, self).__init__(name, description)


class Clock(Item):
    def __init__(self, name, description):
        super(Clock, self).__init__(name, description)


class Compass(Item):
    def __init__(self, name, description):
        super(Compass, self).__init__(name, description)


class Equipment(Item):
    def __init__(self, name, defense, description, value):
        super(Equipment, self).__init__('Something that you wear', 'Equipment')
        self.equip = False
        self.unequip = True
        self.name = name
        self.defense = defense
        self.description = description
        self.value = value


class Chestplatearmor(Equipment):
    def __init__(self, name, description, value, defense=0):
        super(Chestplatearmor, self).__init__(name, defense, description, value,)
        self.defense = defense


class BootsOfSwiftness(Equipment):
    def __init__(self, name, description, value, defense=0):
        super(BootsOfSwiftness, self).__init__(name, defense, description, value)
        self.defense = defense


class PitKey(Item):
    def __init__(self, name, description):
        super(PitKey, self).__init__(name, description)


class Gauntlet(Equipment):
    def __init__(self, name, description, value, defense=0):
        super(Gauntlet, self).__init__(name, defense, description, value)
        self.defense = defense


class SteelSword(Weapons):
    def __init__(self, attack, block, name, description):
        super(SteelSword, self).__init__(attack, block, name, description)


class SteelShield(Weapons):
    def __init__(self, attack, block, name, description):
        super(SteelShield, self).__init__(attack, block, name, description)


class Character(object):
    def __init__(self, name, health, armor, attack, description, dialogue):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        self.description = description
        self.dialogue = dialogue
        self.inventory = []


wooden_sword = WoodenSword(102, 0, 'Wooden Sword', 'A wooden sword')
shield = Shield(0, 41, 'Wooden Shield', 'a wooden shield')
battle_axe = BattleAxe(76, 0, 'Battle Axe', 'A powerful battle axe that was used in battle.')
wings = Wings('Wings', 'wings that can make you fly')
clock = Clock('Clock', 'a clock that tells you the time')
compass = Compass('Compass', 'A compass that tells you what direction you are going')
chestplatearmor = Chestplatearmor('Chestplatearmor', 'a basic armor that will protect you from attacks', 100, 50)
bootsofswiftness = BootsOfSwiftness('Boots of swiftness', 'Boots that make you go faster', 100, 30)
pitkey = PitKey('Pitkey', 'The key that is required to unlock the door in pit')
gauntlet = Gauntlet('Gauntlet', 'Gauntlets that protect nope', 100, 30)
steelsword = SteelSword(205, 0, 'Steel Sword', 'A steel sword that is stronger than a wooden_sword')
steelshield = SteelShield(0, 70, 'Steel Shield', 'a steel shield that is better then a wooden_shield')
dagger = Dagger(38, 0, 'Dagger', 'A dagger that is fast at attacking, and is small that requires little space')


Snapper = Character('Snapper', 320, 0, 50, "Snapper is a turtle , that is seeking to Ionia\n"
                    " so he can deliver a message to the Master", None)

Enemy1 = Character('FireNationTrooper', 200, 0, 50, 'An enemy that wil attack you', None)

Enemy2 = Character('FireNationGuard', 500, 0, 103, 'An enemy that wil attack you', None)

class Room(object):
    def __init__(self, name, north, south, east, west, items, description, enemies):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.description = description
        self.enemies = []

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Intialize Rooms
noxus = Room('noxus', 'top_mid', None, 'outsideoflongdoors', 'outsideoftunnels', None, 'You are in Noxus, you must\n'
                                                                                       ' find a way to get to\n'
                                                                                       ' Ionia', None)
outsideoftunnels = Room('outsideoftunnels', 'tunnels', 'noxus', None, None, wooden_sword, 'You are outside of \n'
                                                                                          'Tunnels', None)
outsideoflongdoors = Room('outsideoflongdoors', 'longdoors', 'noxus', None, 'top_mid', None, 'You are outside\n'
                          'of Long Doors', None)
longdoors = Room('longdoors', None, 'outsideoflongdoors', 'long', None, chestplatearmor, 'You are in\n'
                 ' Long Doors, you see 5 boxes on top of each other', None)
long = Room('long', 'icathia', 'pit', None, 'longdoors', None, 'You are at Long, you see a mist of\n'
            ' clouds north.', None)
tunnels = Room('tunnels', 'howling_marsh', 'outsideoftunnels', 'lower_tunnels', None, battle_axe, 'You are inside\n'
               ' of Tunnels, and you see an axe, you see a staircase leading down from the\n'
               ' east, and light from the north', [Enemy1])
lower_tunnels = Room('lower_tunnels', None, None, 'mid', 'tunnels', compass, 'You are in lower\n'
                     ' tunnels, you see a compass on the table', None)
mid = Room('mid', 'mid_doors', 'top_mid', 'staircase', 'lower_tunnels', None, 'You are at mid and you see a\n'
           'door to the west and a door to the north.', [Enemy2])
pit = Room('pit', 'long', 'pitdoor', 'longdoors', None, clock, 'The pit.. There is a door to the south', None)
pitdoor = Room('pitdoor', 'pit', 'noxus', None, None, wings, 'Where the wings lies. You see the wing on the ground\n'
                                                             'and there is a portal to the south', None)
staircase = Room('staircase', 'shadow_isle', 'top_mid', None, 'mid', None, 'You see a hallway\n'
                 ' turning right, and it is\n'
                 ' leading to a stair case, with dark and misty clouds. As your feet tremble you hear a sound.', None)
shadow_isle = Room('shadow_isle', None, 'staircase', 'icathia', None, gauntlet, 'You\n'
                   ' are finally in the Shadow Isle and there are thick clouds. You feel\n'
                   ' as if someone is watching you, and you see a steel shield laying on the ground.', None)
icathia = Room('icathia', 'goose', 'long', None, 'shadow_isle', bootsofswiftness, 'You are in Icathia, this City\n'
               ' is close to Ionia', None)
ionia = Room('ionia', None, None, None, 'mid_doors', None, 'You have finally reached Ionia, and people\n'
             'welcome you to the City.', None)
goose = Room('goose', None, 'icathia', None, None, steelshield, 'You are in the ally\n'
             ' of goose, it is a small ally wih a small, you see a shield lying on the ground.', None)
howling_marsh = Room('howling_marsh', None, 'tunnels', 'mid_doors', None, steelsword, 'You are in Howling Marsh....\n'
                                                                                      'You feel as very unsafe \n'
                                                                                      'and see dead trees \n'
                                                                                      'everywhere.', None)
top_mid = Room('top_mid', 'mid', 'noxus', 'outsideoflongdoors', None, None, "You don't\n'"
               "see anything particular that is interesting at all. You see a ramp going down to the north.", None)
mid_doors = Room('mid_doors', None, 'mid', 'ionia', 'howling_marsh', None,'You are at mid doors, and to your west you\n'
                 ' see a shadowing place, and to your right is ionia.', None)


current_node = noxus
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']
all_commands = ['yes', 'inv']

while True:
    print(current_node.name)
    print(current_node.description)
    if current_node.items is not None:

        print("Do you wanna pick up item?")
        print(current_node.items.name)

    command = input('>_').lower()

    if command == 'yes':
        print('You took %s.' % current_node.items.name)
        Snapper.inventory.append(current_node.items)
        current_node.items = None

    if current_node.character is not None:
        command = input(">_")
        print("There is an enemy here! The FIRE NATION IS HERE!!")


    if command == 'quit':
        quit(0)
    elif command in short_direction:
        # Look for which command we typed in
        pos = short_direction.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command == 'inv':
        if len(Snapper.inventory) > 0:
            for i in Snapper.inventory:
                print(i.name)
        else:
            print("You don't have anything yet")

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    elif command not in all_commands:
        print("Command not Recognized")
    print('')
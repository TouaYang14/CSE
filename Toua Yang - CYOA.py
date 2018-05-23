import random
# import statements
# class definitions
# items
# characters
# rooms
# instantiate classes
# controller

print("__           ________ _      _____ ____  __  __ ______ \n"
" \ \        / /  ____| |    / ____/ __ \|  \/  |  ____|\n"
"  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   \n"
"   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  \n"
"    \  /\  /  | |____| |___| |___| |__| | |  | | |____ \n"
"     \/  \/   |______|______\_____\____/|_|  |_|______|")


class Item(object):
    def __init__(self, name, description):
        self.equip = False
        self.unequip = True
        self.name = name
        self.description = description


class Weapons(Item):
    def __init__(self, damage, block, name, description):
        super(Weapons, self).__init__('Tools that you use to do damage', 'Weapons')
        self.equip = False
        self.unequip = True
        self.damage = damage
        self.block = block
        self.name = name
        self.description = description


class Dagger(Weapons):
    def __init__(self, damage, block, name, description):
        super(Dagger, self).__init__(damage, block, name, description)


class WoodenSword(Weapons):
    def __init__(self, damage, block, name, description):
        super(WoodenSword, self).__init__(damage, block, name, description)


class Shield(Weapons):
    def __init__(self, damage, block, name, description):
        super(Shield, self).__init__(damage, block, name, description)


class BattleAxe(Weapons):
    def __init__(self, damage, block, name, description):
        super(BattleAxe, self).__init__(damage, block, name, description)


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


class Rock(Item):
     def __init__(self, name, description):
        super(Rock, self).__init__(name, description)


class PitKey(Item):
    def __init__(self, name, description):
        super(PitKey, self).__init__(name, description)


class Gauntlet(Equipment):
    def __init__(self, name, description, value, defense=0):
        super(Gauntlet, self).__init__(name, defense, description, value)
        self.defense = defense


class SteelSword(Weapons):
    def __init__(self, damage, block, name, description):
        super(SteelSword, self).__init__(damage, block, name, description)


class SteelShield(Weapons):
    def __init__(self, damage, block, name, description):
        super(SteelShield, self).__init__(damage, block, name, description)


class Character(object):
    def __init__(self, name, health, armor, damage, description, dialogue, max_hp):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self.description = description
        self.dialogue = dialogue
        self.inventory = []
        self.max_hp = max_hp

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0


wooden_sword = WoodenSword(102, 0, 'Wooden Sword', 'A wooden sword')
shield = Shield(0, 41, 'Wooden Shield', 'a wooden shield')
battle_axe = BattleAxe(76, 0, 'Battle Axe', 'A powerful battle axe that was used in battle.')
wings = Wings('Wings', 'wings that can make you fly')
clock = Clock('Clock', 'a clock that tells you the time')
compass = Compass('Compass', 'A compass that tells you what direction you are going')
chestplatearmor = Chestplatearmor('Chestplatearmor', 'a basic armor that will protect you from damage', 100, 50)
rock = Rock('Rock', 'A rock that is used for nothing')
pitkey = PitKey('Pitkey', 'The key that is required to unlock the door in pit')
gauntlet = Gauntlet('Gauntlet', 'Gauntlets that protect nope', 100, 30)
steelsword = SteelSword(205, 0, 'Steel Sword', 'A steel sword that is stronger than a wooden_sword')
steelshield = SteelShield(0, 70, 'Steel Shield', 'a steel shield that is better then a wooden_shield')
dagger = Dagger(38, 0, 'Dagger', 'A dagger that is fast at attacking, and is small that requires little space')


Snapper = Character('Snapper', 320, 0, 50, "Snapper is a turtle , that is seeking to Ionia\n"
                    " so he can deliver a message to the Master", None, 320)

Enemy1 = Character('FireNationTrooper', 200, 0, 50, 'An enemy that will attack you', None, 200)

Enemy2 = Character('FireNationGuard', 500, 0, 103, 'An enemy that will attack you', None, 500)

Enemy3 = Character('FireNationCaptain', 700, 40, 150, 'THE CAPTAIN OF THE FIRE NATIONS', None, 700)


class Room(object):
    def __init__(self, name, north, south, east, west, items, description, enemies):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.description = description
        self.enemies = enemies

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
               ' east, and light from the north', Enemy1)
lower_tunnels = Room('lower_tunnels', None, None, 'mid', 'tunnels', compass, 'You are in lower\n'
                     ' tunnels, you see a compass on the table', None)
mid = Room('mid', 'mid_doors', 'top_mid', 'staircase', 'lower_tunnels', None, 'You are at mid and you see a\n'
           'door to the west and a door to the north.', Enemy2)
pit = Room('pit', 'long', 'pitdoor', 'longdoors', None, clock, 'The pit.. There is a door to the south', None)
pitdoor = Room('pitdoor', 'pit', 'noxus', None, None, wings, 'Where the wings lies. You see the wing on the ground\n'
                                                             'and there is a portal to the south', None)
staircase = Room('staircase', 'shadow_isle', 'top_mid', None, 'mid', dagger, 'You see a hallway\n'
                 ' turning right, and it is\n'
                 ' leading to a stair case, with dark and misty clouds. As your feet tremble you hear a sound.', None)
shadow_isle = Room('shadow_isle', None, 'staircase', 'icathia', None, gauntlet, 'You\n'
                   ' are finally in the Shadow Isle and there are thick clouds. You feel\n'
                   ' as if someone is watching you, and you see a steel shield laying on the ground.', None)
icathia = Room('icathia', 'goose', 'long', None, 'shadow_isle', rock, 'You are in Icathia, this City\n'
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
mid_doors = Room('mid_doors', None, 'mid', 'ionia', 'howling_marsh', None,
                 'You are at mid doors, and to your west you\n'
                 ' see a shadowing place, and to your right is ionia.', Enemy3)

current_node = noxus
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']
all_commands = ['yes', 'inv']

while True:
    if current_node == noxus:
        if Snapper.health < Snapper.max_hp:
            Snapper.health = Snapper.max_hp
    print(current_node.name)
    print(current_node.description)
    if current_node.items is not None:
        print("Do you wanna pick up item?")
        print(current_node.items.name)
        command = input('>_').lower()
        if command == 'yes':
            weapon_class = [dagger, wooden_sword, steelsword, battle_axe]
            print('You took %s.' % current_node.items.name)
            if current_node.items in weapon_class:
                Snapper.damage += current_node.items.damage
                print("You damage now is %s" % Snapper.damage)
            Snapper.inventory.append(current_node.items)
            current_node.items = None

        else:
            if command == 'no':
                print("You did not pick up the item")
    if current_node.enemies is not None:
        print("There is an Enemy here. IT'S THE %s" % current_node.enemies.name)
        print("What do you want to do?")
        command = input('>_').lower()
        if command == 'fight':
            print("You engaged into the %s" % current_node.enemies.name)
            print("What do you want to do?")
            print("\n1: Attack\n2: Run")
            run = 0
            while Snapper.health > 0 and current_node.enemies.health > 0 and run == 0:
                command = input(">_")
                if command == '1':
                    current_node.enemies.health -= Snapper.damage
                    Snapper.take_damage(current_node.enemies.damage)
                    print('You attacked the %s' % current_node.enemies.name)
                    print('It takes %s damage' % Snapper.damage)
                    if current_node.enemies.health > 0:
                        print('It has %s health left' % current_node.enemies.health)
                    else:
                        print('It has 0 health left')
                    if current_node.enemies.health >= 1:
                        print("The %s attacked you" % current_node.enemies.name)
                        print('It does %s damage' % current_node.enemies.damage)
                        print("YOUR HP: %s" % Snapper.health)
                    if current_node.enemies.health == 0:
                        # current_node.enemies.health = 0
                        print("The %s died" % current_node.enemies.name)
                        current_node.enemies = None
                    if Snapper.health < 0:
                        print("You have died")
                        print("Game Over")
                        exit(0)

                    print()
                    print("What do you want to do?")
                    print("\n1: Attack\n2: Run")
                if command == '2':
                    luck = random.randint(1, 1)
                    if luck == 1:
                        run += 1
                        print("You run away.")
                    if luck != 1:
                        print("You cannot run away\n"
                              ""
                              "the %s is preventing you from running away" % current_node.enemies.name)

    command = input('>_').lower()
    if command in short_direction:
        pos = short_direction.index(command)
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

    if command == 'quit':
            quit(0)

    print('')

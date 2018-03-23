class Room(object):
    def __init__(self, name, north, south, east, west, items, item2, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.item2 = item2
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Intialize Rooms
noxus = Room('noxus', 'top_mid', None, 'outsideoflongdoors', 'outsideoftunnels', 'Wooden_sword', 'Wooden_shield', '\n'
             'You are in Noxus, you must find a way to get to Ionia')
outsideoftunnels = Room('outsideoftunnels', 'tunnels', 'noxus', None, None, None, None, 'You are outside of Tunnels')
outsideoflongdoors = Room('outsideoflongdoors', 'long', 'noxus', None, 'top_mid', None, None, 'You are outside\n'
                          ' of Long Doors')
longdoors = Room('longdoors', None, 'outsideoflondoors', None, 'long', 'Smoke_Capsule', None, 'You are in\n'
                 ' Long Doors, you see 5 boxes on top of each other')
long = Room('long', 'icathia', 'outsideoflongdoors', None, None, None, None, 'You are at Long, you see a mist of\n'
            ' clouds north.')
tunnels = Room('tunnels', 'howling_marsh', 'outsideoftunnels', 'lower_tunnels', None, 'Battle_Axe', '\n'
               'small_health_potion', 'You are inside\n'
               ' of Tunnels, you see a staircase leading down from the east, and light from the north')
lowertunnels = Room('lowertunnels', None, None, 'mid', 'tunnels', 'Clock', 'Compass', 'You are in lower tunnels, you\n'
                    'see a clock and a compass on the table')
mid = Room('mid', 'mid_doors', 'top_mid', 'staircase', 'lowertunnels', None, None, 'You are at mid and you see a door\n'
           'north, you see a hallway leading to a stair to the east.')
staircase = Room('staircase', 'shadow_isle', 'top_mid', None, 'mid', None, None, 'You see a hallway\n'
                 ' turning right, and it is\n'
                 ' leading to a stair case, with dark and misty clouds. As your feet tremble you hear a sound.')
shadow_isle = Room('shadow_isle', None, 'staircase', 'icathia', None, 'shadow_hammer', None, 'You\n'
                   ' are finally in the Shadow Isle and there are thick clouds. You feel\n'
                   ' as if someone is watching you, and you see a hammer laying on the ground.')
icathia = Room('icathia', 'goose', 'long', None, 'shadow_isle', 'wings', None, 'You are in icathia and you\n'
               ' a pair of wings lying on the ground')
ionia = Room('ionia', None, None, 'shadow_isle', 'mid_doors', None, None, 'You have finally reached Ionia.')
goose = Room('goose', None, 'icathia', None, None, 'egg', None, 'You are in the ally\n'
             ' of goose, it is a small ally wih a small, you see an egg lying on the ground.')
howling_marsh = Room('howling_marsh', None, 'tunnels', 'mid_doors', None, 'fogoggles', None, 'You are in Howling\n'
                     ' Marsh.... You feel as very unsafe and see dead trees everywhere.')
top_mid = Room('top_mid', 'mid', 'noxus', 'outsideoflongdoors', None, None, None, "You\n'"
               "are at the top of mid. You don't see\n"
               " anything particular that is interesting at all. You see a ramp going down to the north.")
mid_doors = Room('mid_doors', None, 'mid', 'ionia', 'howling_marsh', None, None, 'You\n'
                 ' are at mid doors, and to your west you see a shadowing place, and to your right is ionia.')

current_node = noxus
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']

while True:
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

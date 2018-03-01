class Room(object):
    def __init__(self, name, north, south, east, west, items, item2,  description):
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
noxus = Room('noxus', 'top_mid', None, 'outsideoflongdoors', 'outsideoftunnels', 'wooden_sword', 'wooden_shield', '\n'
             'You are in Noxus, you must find a way to get to Ionia')
outsideoftunnels = Room('outsideoftunnels', 'tunnels', 'noxus', None, None, None, None, 'You are outside of Tunnels')
outsideoflongdoors = Room('outsideoflongdoors', 'long', 'noxus', None, 'top_mid', None, None, 'You are outside\n'
                          ' of Long Doors')
longdoors = Room('longdoors', None, 'outsideoflondoors', None, 'long', 'smoke_capsule', None, 'You are in\n'
                 ' Long Doors, you see 5 boxes on top of each other')
long = Room('long', 'Icathia', 'outsideoflongdoors', None, None, None, None, 'You are at Long, you see a mist of\n'
            ' clouds north, and a pit south')
tunnels = Room('tunnels', 'howling_marsh', 'outsideoftunnels', 'lower_tunnels', None, 'battle_axe', '\n'
               'small_health_potion', 'You are inside\n'
               ' of Tunnels, you see a staircase leading down from the east, and light from the north')
lowertunnels = Room('lowertunnels', None, None, 'mid', 'tunnels', 'clock', 'compass', 'You are in lower tunnels, you\n'
                    'see a clock and a compass on the table')
mid = Room('mid', 'mid_doors', 'top_mid', 'staircase', 'lowertunnels', None, None, 'You are at mid and you see a door\n'
           'north, you see a hallway leading to a stair to the east.')
staircase = ('staircase', None, 'top_mid', None, 'mid', None, None, 'You see a hallway turning right, and it is\n'
             ' leading to a stair case, with dark and misty clouds. As your feet tremble you hear a sound.')

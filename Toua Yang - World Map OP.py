class Room(object):
    def __init__(self, name, north, south, east, west, items, description):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.items = items
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Intialize Rooms
west_house = Room("West of House", 'north_house', None)
east_house = Room("East of House", 'west_house', None)
north_house = Room("North of House", 'east_house', None)

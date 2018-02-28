world_map = {
    'NOXUS': {
        'NAME': "Noxus",
        'DESCRIPTION': "You are in Noxus, you must find a way to get to Ionia",
        'PATHS': {
            'NORTH': 'TOPMID',
            'EAST': 'OUTSIDEOFLONGDOORS',
            'WEST': 'OUTSIDEOFTUNNELS'
        }

    },
    'TOPMID': {
        'NAME': 'Top of Mid',
        'DESCRIPTION': "You are at the Top of Mid",
        'PATHS': {
            'SOUTH': 'NOXUS',
            'EAST': 'OUTSIDEOFLONGDOORS',
            'NORTH': 'MID'
        }

    },
    'OUTSIDEOFLONGDOORS': {
        'NAME': 'Outside of Long Doors',
        'DESCRIPTION': "You are outside of Long Doors",
        'PATHS': {
            'NORTH': 'LONGDOORS'
        }
    },
    'LONGDOORS': {
        'NAME': 'Long Doors',
        'DESCRIPTION': "You are in Long Doors, you see 5 boxes on top of each other",
        'PATHS': {
            'NORTH': 'LONG',
            'SOUTH': 'OUTSIDEOFLONGDOORS'
        }
    },
    'OUTSIDEOFTUNNELS': {
        'NAME': 'Outside of Tunnels',
        'DESCRIPTION': "You are outside of Tunnels",
        'PATHS': {
            'NORTH': 'TUNNELS',
            'SOUTH': 'NOXUS'
        }
    },
    'TUNNELS': {
        'NAME': 'Tunnels',
        'DESCRIPTION': "You are inside of Tunnels, you see a staircase leading down from the east, and light from the north",
        'PATHS': {
            'NORTH': 'HOWLING MARSH',
            'SOUTH': 'OUTSIDEOFTUNNELS',
            'EAST': 'LOWERTUNNELS'
        }
    },
    'HOWLING MARSH': {
        'NAME': 'Howling Marsh',
        'DESCRIPTION': "You are in Howling Marsh, the air around you becomes thick and you feel as if someone is watching you... You see a window to the east that is broken but light is coming from it",
        'PATHS': {
            'EAST': ' ROADTOIONIA'
        }
    },
    'LOWERTUNNELS': {
        'NAME': 'Lower Tunnels',
        'DESCRIPTION': "You are in Lower Tunnels, the room is thin and is very dusty, you see a light coming from the east, and stairs going up leading to the west...",
        'PATHS': {
            'EAST': 'XBOX',
            'WEST': 'Tunnels'
        }
    },
    'XBOX': {
        'NAME': 'Xbox',
        'DESCRIPTION': "You are next to xbox and you seem to be able to jump onto it. You see a door next to you as well, as a path to the South...",
        'PATHS': {
            'NORTH': 'MIDDOORS',
            'SOUTH': 'TOPMID',

        }
    },
    'MIDDOORS': 'Mid Doors',
        'DESCRIPTION': "You are at Mid Doors, and there are two paths leading to west and east",
        'PATHS': {
        'EAST': 'IONIA',
        'SOUTH': 'XBOX',
        'WEST': 'HOWLING MARSH'
        }
    },
    'SHADOWISLE': 'Shadow Isle',
        'DESCRIPTION': "You are in the Shadow Isle and the air became thick again.. It is very foggy and dark..",
        'PATHS': {
            'EAST': 'ICATHIA',
            'WEST': 'IONIA'
    }
}

current_node = world_map['NOXUS'],
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not Recognized")
    print()
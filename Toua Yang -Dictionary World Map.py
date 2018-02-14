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
            'SOUTH': 'NOXUS'
        }

    },
    'OUTSIDEOFLONGDOORS': {
        'NAME': 'Outside of Long Doors',
        'DESCRIPTION': "You are outside of Long Doors",
        'PATHS': {
            'NORTH': 'LONGDOORS'
        }
    },
    'OUTSIDEOFTUNNELS': {
        'NAME': 'Outside of Tunnels',
        'DESCRIPTION': "You are outside of Tunnels",
        'PATHS': {
            'NORTH': 'LONGDOORS'
            'SOUTH': 'OUTSIDEOFLONGDOORS'
        }
    }
}

current_node = world_map['NOXUS']
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
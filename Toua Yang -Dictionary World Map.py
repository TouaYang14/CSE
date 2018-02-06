world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of Huse',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'SOUTH': 'WESTHOUSE'
        }

    },
    'SOUTHHOUSE': {
        'NAME': 'South of Huse',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    },
}
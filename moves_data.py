# moves_data.py

moves = {
    'Growl': {
        'name': 'Growl',
        'type': 'Normal',
        'category': 'Status',
        'power': 0,
        'accuracy': 100,
        'effect': {
            'stat_change': {
                'attack': -1
            },
            'target': 'opponent'
        }
    },
    'Scratch': {
        'name': 'Scratch',
        'power': 10,
        'type': 'Normal',
        'category': 'Physical'
    },
    'Ember': {
        'name': 'Ember',
        'power': 25,
        'type': 'Fire',
        'category': 'Special',
        'effect': {
            'status': 'Burned',
            'chance': 10,
            'target': 'opponent'
        }
    },
    'Poison Sting': {
        'name': 'Poison Sting',
        'power': 15,
        'type': 'Poison',
        'category': 'Physical',
        'effect': {
            'status': 'Poisoned',
            'chance': 80,
            'target': 'opponent'
        }
    },
    'Stomp': {
        'name': 'Stomp',
        'power': 20,
        'type': 'Normal',
        'category': 'Physical'
    },
    'Water Spout': {
        'name': 'Water Spout',
        'power': 20,
        'type': 'Water',
        'category': 'Special'
    }
}

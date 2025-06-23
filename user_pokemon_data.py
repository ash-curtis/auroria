# user_pokemon_data.py


class Pokemon:

    def __init__(self, name, pokemon_type, moves, status, stats):
        self.name = name
        self.pokemon_type = pokemon_type
        self.moves = moves
        self.status = status
        self.stats = stats
        self.status_condition = None

    def take_damage(self, damage_amount):
        self.stats['hp'] -= damage_amount  # reduce the pokemon's hp
        if self.stats['hp'] < 0:  # make sure damage doesn't go below zero
            self.stats['hp'] = 0
        print(f"{self.name} took {damage_amount} damage!")
        print(f"{self.name} now has {self.stats['hp']} HP left.")

    def apply_status(self, new_status):
        if self.status_condition is None:  # only if no status is active
            self.status_condition = new_status
            print(f"{self.name} became {new_status}!")
        else:
            print(
                f"{self.name} is already {self.status_condition} and cannot be {new_status}!"
            )

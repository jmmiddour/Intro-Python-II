# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __repr__(self):
        return f'{self.items}'

# __str__ : intended to be human readable
# __repr__: explict for development
from room import Room
from player import Player
import random
from item import Item

# Declare all items
inventory = {
    'everfill': Item('Everfill Bag', 'Never have to empty it, just keep adding to it.'),
    'sword':    Item('Sword', '4 feet of lovely, shiney blade with a beautiful golden hilt.'),
    'h_potion': Item('Healing Potion', 'This potion will restore your health to 100%.'),
    'e_potion': Item('Exploding Potion', 'A round glass bottle that can be thrown to distract your enemy.'),
    'dagger':   Item('Dagger', 'A glorious 8 inch blade with an edge on each side and a shiney golden hilt.'),
    'w_shield': Item('Wood Shield', 'This wooden shield is adorned with beautiful gems and bares the crest of the royal family.'),
    'm_shield': Item('Metal Shield', 'Shiney silver metal shield with the crest of the royal family and lined with gold trim.'),
    'torch':    Item('Torch', 'The torch is still lit and a great way to help you see in those dark caves.'),
    'staff':    Item('Staff of Eygpt', 'A beautiful work of art, this wooden staff has a carving of Anubis at the top.'),
    'axe':      Item('Battle Axe', 'A medieval double edge battle axe in almost new condition.')
}

# Declare all the rooms
room = {
    'outside':  Room('Outside Cave Entrance', 'North of you, the cave mount beckons',
                     inventory[random.choice(list(inventory.keys()))]),
    'foyer':    Room('Foyer', 'Dim light filters in from the south.\n    Dusty passages run north and east.',
                     inventory[random.choice(list(inventory.keys()))]),
    'overlook': Room('Grand Overlook', 'A steep cliff appears before you, falling into the darkness.\
        \nAhead to the north, a light flickers in the distance, but there is no way across the chasm.',
        inventory[random.choice(list(inventory.keys()))]),
    'narrow':   Room('Narrow Passage', 'The narrow passage bends here from west to north.\
        \nThe smell of gold permeates the air.',
        inventory[random.choice(list(inventory.keys()))]),
    'treasure': Room('Treasure Chamber', 'You have found the long-lost treasure chamber!\
        \nSadly, it has already been completely emptied by earlier adventurers.\
            \nThe only exit is to the south.', inventory[random.choice(list(inventory.keys()))])
}

# Link rooms together (like a map)
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

##################### Main #######################

# Make a new player object that is currently in the 'outside' room.
player_name = input('What is your name? ')
player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Define a function to handle the direction changes
def room_logic(direction):
    # Check if player input is n, s, e, or w
    if direction == 'n' or direction == 's' or direction == 'e' or direction == 'w':
        move = direction + '_to'

        # If there is nothing in that direction
        if not getattr(player.current_room, move):
            print(f'\nOops, you can not go that way! Going back to {player.current_room.name}.')

        # Move to the new location
        else:
            player.current_room = getattr(player.current_room, move)

    # If the player inputs q to quit the game
    elif direction == 'q':
        print('\nThank you for playing!')

    # If the player inputs an invalid letter
    else: 
        print(f'\nInvalid input, going back to the {player.current_room.name}.')

# Define a function for the inventory items
def inv_items(take_item):
    # If the player wants to take the item
    if take_item.lower() == 'y':
        player.grab(player.current_room.inventory)
        # for i in [player.current_room.inventory]:
        #     [inventory].remove(i)

        # Prompt player with option of removing an item from their inventory
        drop_item = input('\nWould you like to drop an item? y = yes / n = no: ')

        # If the player chooses to remove item from inventory
        if drop_item.lower() == 'y':
            item_to_drop = str(input(f'\nWhat would you like to remove from your inventory? '))
            player.rem_item(item_to_drop)
            print(f'  * This is your inventory now:\n{player.inventory}')

    # Let player know they are leaving the item
    else:
        print(f'\nYou are leaving {player.current_room.inventory.name} behind.')
        print(f'  * This is your current inventory:\n{player.inventory}')

# Create an empty variable to hold the player input
player_input = ''

# Create a loop to keep playing unitl the player types q to quit
while player_input != 'q':
    # Print Player name, current location, and location desscription
    print(f'\n{player_name}, you are currently in the {player.current_room.name}.')
    print(f'  * {player.current_room.description}')

    # Print the item in the room
    print(f'\nYou see something on the ground, it looks like a {player.current_room.inventory.name}.\n  * {player.current_room.inventory.description}\n')

    # Prompt user to take or leave item in the room
    take_item = input(f'Do you want to take the {player.current_room.inventory.name}? y = yes / n = no: ')

    # Player chooses to take or leave item using function above
    inv_items(take_item)

    # Prompt player to move to a new location
    player_input = input('''
    Where would you like to go now?
    Type "n" for North, "s" for South, "e" for East, "w" for West, or "q" for quit: ''')

    # Take the player to the new location using the function above
    room_logic(player_input)

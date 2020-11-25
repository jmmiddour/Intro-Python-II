from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Dixie', room['outside'])

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

# This is one way to do it:
# user_input = ''
# while user_input != 'q':
#     print('You are currently in the', new_player.current_room.name, '\n')
#     print(new_player.current_room.description)

#     user_input = input('''
#     Where would you like to go now?
#     Type "n" for North, "s" for South, "e" for East, "w" for West, or "q" for quit: ''')
#     print()

#     if user_input == 'n':
#         if new_player.current_room.n_to == None:
#             print(f'Can not go North. Going back to {new_player.current_room.name}.\n')
#         else:
#             new_player.current_room = new_player.current_room.n_to

#     elif user_input == 's':
#         if new_player.current_room.s_to == None:
#             print(f'Can not go South. Going back to {new_player.current_room.name}.\n')
#         else:
#             new_player.current_room = new_player.current_room.s_to

#     elif user_input == 'e':
#         if new_player.current_room.e_to == None:
#             print(f'Can not go East. Going back to {new_player.current_room.name}.\n')
#         else:
#             new_player.current_room = new_player.current_room.e_to

#     elif user_input == 'w':
#         if new_player.current_room.w_to == None:
#             print(f'Can not go West. Going back to {new_player.current_room.name}.\n')
#         else:
#             new_player.current_room = new_player.current_room.w_to

#     elif user_input == 'q':
#         print('Thank you for playing!')
    
#     else:
#         print(f'Invalid input, going back to {new_player.current_room.name}.\n')


# A shorter way to do the same as above:
def room_logic(direction):
    if direction=='n' or direction=='s' or direction=='e' or direction=='w':
        move = direction + '_to'
        if not getattr(new_player.current_room, move):
            print(f'\nOops, can not go that way! Going back to {new_player.current_room.name}.')
        else:
            new_player.current_room = getattr(new_player.current_room, move)

    elif direction == 'q':
        print('\nThank you for playing!')

    else: 
        print(f'\nInvalid input, going back to the {new_player.current_room.name}.')

player_input = ''

while player_input != 'q':
    print('\nYou are currently in the', new_player.current_room.name, '\n')
    print(new_player.current_room.description)
    
    player_input = input('''
    Where would you like to go now?
    Type "n" for North, "s" for South, "e" for East, "w" for West, or "q" for quit: ''')
    
    room_logic(player_input)
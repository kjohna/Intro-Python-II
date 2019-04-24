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


# Link rooms together

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
player = Player("player name", room['outside'])
print('\n\nWelcome to **ADVENTURES** in Python\n\n')

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print(f"You find yourself {player.location.name}")
print(f"{player.location.desc}")

# * Waits for user input and decides what to do.
instructions = 'Move [n], [e], [s], or [w]. [q] to quit.\n >  '
u_input = input(f'\nPlease decide what to do: {instructions}').lower()
while not u_input == 'q':
    # If the user enters a cardinal direction, attempt to move to that room.
    # Print an error message if the movement isn't allowed.
    if u_input == 'n':
        print('Move North')
    elif u_input == 'e':
        print('Move East')
    elif u_input == 's':
        print('Move South')
    elif u_input == 'w':
        print('Move West')
    # Any other input
    else:
        print(f'Invalid input.')
    # prompt after each input
    u_input = input(f'\nPlease decide what to do: {instructions}').lower()

# End of u_input loop: if the user enters "q", quit the game.
print("\n\nAdventure complete! Quitting..\n\n")

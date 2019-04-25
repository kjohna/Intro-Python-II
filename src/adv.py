from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        ["rock", "wood", "stick"]
    ),
    'foyer':    Room("In a Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("At a Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("In a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("In the Treasure Chamber", """You've found the long-lost treasure
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
player.location.describe_room()

# * Waits for user input and decides what to do.
instructions = 'Move [n], [e], [s], or [w]. [q] to quit.\n >  '
u_input = input(f'\nPlease decide what to do: {instructions}').lower()
while not u_input == 'q':
    # If the user enters a cardinal direction, attempt to move to that room.
    # Print an error message if the movement isn't allowed.
    if u_input == 'n':
        if player.location.n_to:
            player.move_to(player.location.n_to)
        else:
            print('There is nothing to the North!')
    elif u_input == 'e':
        if player.location.e_to:
            player.move_to(player.location.e_to)
        else:
            print('There is nothing to the East!')
    elif u_input == 's':
        if player.location.s_to:
            player.move_to(player.location.s_to)
        else:
            print('There is nothing to the South!')
    elif u_input == 'w':
        if player.location.w_to:
            player.move_to(player.location.w_to)
        else:
            print('There is nothing to the West!')
    # Any other input
    else:
        print(f'Invalid input.')
    # prompt after each input
    u_input = input(f'\nPlease decide what to do: {instructions}').lower()

# End of u_input loop: if the user enters "q", quit the game.
print("\n\nAdventure complete! Quitting..\n\n")

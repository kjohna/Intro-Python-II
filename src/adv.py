from item import Item, LightSource
from player import Player
from room import Room

# Declare Items
item = {
    'rock': Item("rock", "An ordinary rock"),
    'wood': Item("wood", "A piece of lumber."),
    'stick': Item("stick", "A piece of a tree."),
    'torch': LightSource("torch", "A standard torch.", False)
}

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside",
        "Cave Entrance",
        "North of you, the cave mount beckons",
        [item['rock'], item['wood'], item['stick'], item['torch']]
    ),
    'foyer':    Room("In a", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("At a", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("In a", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("In the", "Treasure Chamber", """You've found the long-lost treasure
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
print(player.location)
# * Waits for user input and decides what to do.
instructions = '''\nMove [n], [e], [s], or [w].
    \n[take item] or [drop item] to take or drop items around you.
    \n[i] or [inventory] to see items in your inventory.
    \n[l] to look around the current room.
    \n[q] to quit.'''
u_input = input(
    f'\nPlease decide what to do. [help] for available commands.\n> ')\
    .lower()\
    .split(" ")
while not u_input[0] == 'q':
    u_input_len = len(u_input)
    # single command
    if u_input_len == 1:
        # If the user enters a cardinal direction, attempt to move to that room
        # Print an error message if the movement isn't allowed.
        if u_input[0] == 'n':
            if player.location.n_to:
                player.move_to(player.location.n_to)
            else:
                print('There is nothing to the North!')
        elif u_input[0] == 'e':
            if player.location.e_to:
                player.move_to(player.location.e_to)
            else:
                print('There is nothing to the East!')
        elif u_input[0] == 's':
            if player.location.s_to:
                player.move_to(player.location.s_to)
            else:
                print('There is nothing to the South!')
        elif u_input[0] == 'w':
            if player.location.w_to:
                player.move_to(player.location.w_to)
            else:
                print('There is nothing to the West!')
        elif u_input[0] == 'i' or u_input[0] == 'inventory':
            player.desc_inventory()
        elif u_input[0] == 'l':
            player.location.desc_inventory()
        elif u_input[0] == 'help':
            print(instructions)
        else:
            print(f'Invalid input.')
    # double command
    elif u_input_len == 2:
        # assume first part is verb, second is noun
        verb = u_input[0]
        noun = u_input[1]
        if verb == 'take':
            if player.location.remove_item(player, noun):
                player.desc_inventory()
                player.location.desc_inventory()
            else:
                print(f'There is no {noun} here.')
        elif verb == 'drop':
            if player.drop_item(noun):
                player.desc_inventory()
                player.location.desc_inventory()
            else:
                print(f'You do not have {noun}.')
        else:
            print(f'Your player does not know how to {verb}.')
    # Any other input
    else:
        print(f'Invalid input.')
    # prompt after each input
    u_input = input(
        f'\nPlease decide what to do. [help] for available commands.\n> ')\
        .lower()\
        .split(" ")

# End of u_input loop: if the user enters "q", quit the game.
print("\n\nAdventure complete! Quitting..\n\n")

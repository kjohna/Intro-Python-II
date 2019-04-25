# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    def move_to(self, new_loc):
        self.location = new_loc
        print(self.location)

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item_name):
        # look for item in player's inventory.
        # player drops first item matching description, return True.
        # if none found, return False
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.location.add_item(item)
                self.items.pop(i)
                return True
        return False

    def desc_inventory(self):
        if len(self.items):
            print('Your inventory: ')
            print(*self.items, sep="\n")
        else:
            print('You have no items.')

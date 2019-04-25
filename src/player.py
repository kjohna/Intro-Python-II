# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items
        self.is_providing_light = False

    def move_to(self, new_loc):
        # player no longer provides light to room being left
        self.location.player_lit = False
        self.location = new_loc
        # if player is providing light, light the new room
        if self.is_providing_light:
            self.location.player_lit = True
        print(self.location)

    def has_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                return item
        return False

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

    def provide_light(self, providing):
        self.is_providing_light = providing
        self.location.player_lit = providing
        print(self.location)

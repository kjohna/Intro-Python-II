# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    def move_to(self, new_loc):
        self.location = new_loc
        self.location.describe_room()

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        prev_items = self.items[:]
        self.items = [filter(
            lambda item: item.name != item_name,
            prev_items
        )]

    def desc_inventory(self):
        if len(self.items):
            print('Your inventory: ')
            print(*self.items, sep="\n")
        else:
            print('You have no items.')

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    def move_to(self, new_loc):
        self.location = new_loc
        self.location.desc_room()
        self.location.desc_inventory()

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item_name):
        prev_items = self.items[:]
        self.items = [item for item in prev_items if item['name'] != item_name]
        if len(prev_items) > len(self.items):
            return True
        else:
            return False

    def desc_inventory(self):
        if len(self.items):
            print('Your inventory: ')
            print(*self.items, sep="\n")
        else:
            print('You have no items.')

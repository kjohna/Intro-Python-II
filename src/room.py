# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        # connected to the room:
        self.n_to = False
        self.e_to = False
        self.s_to = False
        self.w_to = False
        # contained within room:
        self.items = items

    def desc_room(self):
        print(f"You find yourself {self.name}")
        print(f"{self.desc}")

    def desc_inventory(self):
        if len(self.items):
            print("Around you you see: ")
            print(*self.items, sep="\n")
        else:
            print('The room is empty.')

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, player, item_name):
        # look for item in room's inventory.
        # player takes first item matching description, return True.
        # if none found, return False
        for i, item in enumerate(self.items):
            if item.name == item_name:
                player.take_item(item)
                self.items.pop(i)
                return True
        return False

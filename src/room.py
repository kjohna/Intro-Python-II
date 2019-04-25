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

    def describe_room(self):
        print(f"You find yourself {self.name}")
        print(f"{self.desc}")
        if len(self.items):
            print("Around you you see: ")
            print(*self.items, sep="\n")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        prev_items = self.items[:]
        self.items = [item for item in prev_items if item['name'] != item_name]
        if len(prev_items) > len(self.items):
            return True
        else:
            return False

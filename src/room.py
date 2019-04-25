# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, prefix, name, desc, items=[]):
        self.prefix = prefix
        self.name = name
        self.desc = desc
        # connected to the room:
        self.n_to = False
        self.e_to = False
        self.s_to = False
        self.w_to = False
        # contained within room:
        self.items = items

    def __str__(self):
        # prints user-relevant info about room:
        info = ''
        # room name/description
        info += f'You find yourself {self.prefix} {self.name}\n{self.desc}\n'
        # exits
        if self.n_to:
            info += f'[n] to {self.n_to.name}\n'
        if self.e_to:
            info += f'[e] to {self.e_to.name}\n'
        if self.s_to:
            info += f'[s] to {self.s_to.name}\n'
        if self.w_to:
            info += f'[w] to {self.w_to.name}\n'
        # inventory
        if len(self.items):
            info += 'Around you you see: \n'
            info += '\n'.join([str(item) for item in self.items])
        else:
            info += 'The room is empty.\n'
        return info

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

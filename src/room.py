# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        # connected to the room:
        self.n_to = False
        self.e_to = False
        self.s_to = False
        self.w_to = False

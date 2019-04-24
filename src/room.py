# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

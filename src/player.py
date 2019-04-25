# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_to(self, new_loc):
        self.location = new_loc
        self.location.describe_room()

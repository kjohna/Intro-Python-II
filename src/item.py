# an Item class, base class for specialized items


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"* {self.name} - {self.desc}"

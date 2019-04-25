# an Item class, base class for specialized items


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"* {self.name} - {self.desc}"


class LightSource(Item):
    def __init__(self, name, desc, is_lit=False):
        Item.__init__(self, name, desc)
        self.is_lit = is_lit

    def __str__(self):
        if self.is_lit:
            lit = 'currently lit.'
        else:
            lit = 'not lit.'
        return f"* {self.name} - {self.desc} - {lit}"

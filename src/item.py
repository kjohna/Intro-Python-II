# an Item class, base class for specialized items
import textwrap


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f'* {self.name} - {self.desc}'

    def selected(self):
        wrapper = textwrap.TextWrapper(width=50)
        s = f'\
          This is a really nice {self.name}.\
          You should be grateful to have {self.desc.lower()}.'
        text = textwrap.dedent(s)
        print(text)


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

    def selected(self, player):
        if self.is_lit:
            u_input = input(
                f'The {self.name} is lit.\
                   Would you like to extinguish the torch? [y] [n] \n > ')
            if u_input == 'y':
                self.is_lit = False
                print(f'The {self.name} is extinguished. Hooray!\n')
                player.provide_light(False)
        else:
            u_input = input(
                f'The {self.name} is not lit.\
                   Would you like to light the torch? [y] [n] \n > ')
            if u_input == 'y':
                self.is_lit = True
                print(f'The {self.name} is lit. Hooray!\n')
                player.provide_light(True)

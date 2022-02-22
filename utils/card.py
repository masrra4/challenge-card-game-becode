###DONT FORGET STRING FUN IN EACH CLASS


icon_list=["Hearts", "Diamonds"," Clubs", "Spades"]


class Symbol:
    def __init__(self, color, icon):
        self.color = 'color'
        self.icon = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __str__(self):  # its important to print the value not the position of the value.
        return "{self.color} {self.icon}".format(self=self)


class Card(Symbol):
    def __init__(self, color, icon, value):
        symbol.self.color = 'color'
        symbol.self.icon = 'icon'
        self.value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']


def __str__(self):  # its important to print the value not the position of the value.
    return "{self.color} {self.icon}".format(self=self)

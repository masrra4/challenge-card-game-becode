###DONT FORGET STRING FUN IN EACH CLASS
class Symbol:
    color = ['red', 'black']
    icon = ["Hearts", "Diamonds", " Clubs", "Spades"]
    def __init__(self,icon=0,color=0):
         self.icon = icon
         self.color = color
    #def __str__(self):  # its important to print the value not the position of the value.
     #   return "{self.color} {self.icon}".format(self=self)
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"{self.color} {self.icon}"

class Card(Symbol):
    value=  ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    def __init__(self, color, icon,value):
        Symbol.__init__(self,color ,icon)
        self.value = value

    def __str__(self):  # its important to print the value not the position of the value.
         return ("{self.color} {self.icon} {self.value}".format(self=self))

    if __name__ == '__main__':
           import doctest

   # doctest.testmod()
    """We have a doctest in the __str__ method to confirm that Card(2, 11) will display as “Queen of Hearts”"""
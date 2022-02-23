"""""""""
5. Let's play
In main.py:

Import everything you need to start the game!
Start the game. You should only run this file to have the game running.
"""
import random
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["spades", "Hearts", "Clubs", "Diamonds"]:
            for v in range(1, 14):  # print("{} of {}".format(v, s))
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):#print(i)
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def drawCard(self):
        return(self.cards.pop())


class Player(object):
   def __init__(self,name):
     self.name= name
     self.hand=[]
   def draw(self,deck):
     self.hand.append(deck.drawCard())
     return(self)
   def showHand(self):
       for card in self.hand:
           card.show()
   def Discard(self):
       return self.hand.pop()


# card=Card("clubs",6)
# card.show()
deck = Deck()
deck.shuffle()
#deck.build()
#deck.show()
FirstPlayer=Player("bob")
FirstPlayer.draw(deck)
FirstPlayer.showHand()
SecondPlayer=Player("Rob")
SecondPlayer.draw(deck)
SecondPlayer.showHand()
SecondPlayer=Player("MYA")
SecondPlayer.draw(deck)
SecondPlayer.showHand()
SecondPlayer=Player("Mas")
SecondPlayer.draw(deck)
SecondPlayer.showHand()
#card=deck.draw()
#card.show()

import random

player_one_score = 0
player_Two_score = 0
player_Three_score = 0
player_Four_score = 0
deck=[]
def populate_deck():
    for suit in ("Hearts","Diamond","Clubs",'Speeds'):
        for rank in range(2,15):
            deck.append((rank,suit))
def printable_card(card):
         if card[0]<=10 : rank =str(card[0])
         if card[0]==11 : rank ="Jack"
         if card[0] == 12: rank = "Queen"
         if card[0] == 13: rank = "King"
         if card[0] == 14: rank = "Ace"
         fullname=rank +' of '+card[1]
         return fullname
def draw_card(player):
    card=deck[0]
    deck.remove(deck[0])
    print(player+' drew the  '+printable_card(card))
    return card
#make the deck
populate_deck()
#print(deck)
#shuffle the deck
random.shuffle(deck)
#print(deck)
#every turn
while True:
 #each player draws card
 print(" Player one :which Card Do you want to play?!")
 player_one_card=draw_card("player one")
 print(" Player Two :which Card Do you want to play?!")
 player_Two_card=draw_card("player Two")
 print(" Player Three :which Card Do you want to play?!")
 player_Three_card=draw_card("player Three")
 print(" Player Four :which Card Do you want to play?!")
 player_Four_card=draw_card("player Four")
 # compare to see who wins
 if player_one_card[0]>player_Two_card[0]and player_one_card[0]>player_Three_card[0]and player_one_card[0]>player_Four_card[0]:
     player_one_score+=1
     winner="player one "
     player_one_score +=2
 elif player_Two_card[0] > player_one_card[0] and player_Two_card[0] > player_Three_card[0] and player_Two_card[0] > player_Four_card[0]:
     player_Two_score += 1
     winner = "player Two "
     player_Two_score += 2
 elif player_Three_card[0] > player_one_card[0] and player_Three_card[0] > player_Two_card[0] and player_Three_card[0] > player_Four_card[0]:
     player_Three_score += 1
     winner = "player Three "
     #player_Three_score += 2
 elif player_Four_card[0] > player_one_card[0] and player_Four_card[0] > player_Two_card[0] and player_Four_card[0] > player_Three_card[0]:
     player_Four_score += 1
     winner = "player Four"
     #player_Four_score += 2
 else :winner=' No one '
 print(winner +" wins ")


#tiebreaker
#keep score
#check weather the deck is empty
 if len(deck)==0:
    print("Game over ")
    #print("player one: "+str(player_one_score))

    if player_one_score > player_Two_score and player_one_score > player_Three_score and player_one_score > player_Four_score:
        print('The winner is the First player and he has ' + str(player_one_score) + ' points ')
    elif player_Two_score > player_one_score and player_Two_score > player_Three_score and player_Two_score > player_Four_score:
            print('The winner is the Second player and he has ' + str(player_Two_score) + ' points')
    elif player_Three_score > player_Two_score and player_Three_score > player_one_score and player_Three_score > player_Four_score:
                print('The winner is the Third player and he has ' + str(player_Three_score) + ' points')
    elif player_Four_score > player_Two_score and player_Four_score > player_one_score and player_Four_score > player_Three_score:
             print('The winner is the Fourth player and he has ' + str(player_Three_score) + ' points')

    else:print("No one win, Repeat the game")
    break

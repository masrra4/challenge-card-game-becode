# challenge-card-game-becode
new project :challenge-card-game
Repository: challenge-card-game-becode
Type of Challenge: Consolidation
Duration: 3 days
Deadline: 23/02/22 4:30 PM
Team challenge : solo

Description :

I should build card game in Python. I should create deck of cards , and split between the different players and each player plays a card at every turn, until there are 
The game is working until each player doesn't have any cards left.
The game generates all the cards.
The game distributes all 
Once you have the basis of a card game, you can go ahead and make a real card game from 
Make the game interactive, at each turn, ask the player which card he/her wants to play.
Create game-over conditions and add the possibility in the game to end because of the aforementioned conditions.
Add points for each player if the card is the most powerful card played that turn.
Select a winner out of the players at the end of the game.

Usage:

or in another words how to do it ?
First of all in the utils folder create 3 files:
card.py
player.py
game.py

In card.py:
Create a class called Symbol with two attributes:
color which is a string.
icon which is a single character out of this list [♥, ♦, ♣, ♠].
1.2 Card
In the same file, create a class Card that inherits from Symbol and add an attribute:
value which is a string (one of ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'])
2. A bunch of players
In player.py create a class Player that contains these attributes:
cards which is a list of Card. (you will need to import Card from card.py). In a real card game, this is equivalent to the cards that the player has in his hands.
turn_count which is an int starting a 0.
number_of_cards which is an int starting at 0.
history which is a list of Card that will contain all the cards played by the player.
And some methods:
play() that will:
randomly pick a Card in cards.
Add the Card to the Player's history.
Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
Return the Card.

3. A complete deck
Create a Deck class that contains:

An attribute cards which is going to contain a list of instances of Card.
A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
A shuffle() method that will shuffle all the list of cards.
A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the players.

4. A board
In game.py create:
A class called Board that contains:
An attribute players that is a list of Player. It will contain all the players that are playing.
An attribute turn_count that is an int.
An attribute active_cards that will contain the last card played by each player.
An attribute history_cards that will contain all the cards played since the start of the game, except for active_cards.
A method start_game() that will:
Start the game,
Fill a Deck,
Distribute the cards of the Deck to the players.
Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
At the end of each turn, print:
The turn count.
The list of active cards.
The number of cards in the history_cards.
In main.py:
Import everything you need to start the game!
Start the game. You should only run this file to have the game running.

(Visuals)
(Contributors) :it is a solo project 
(Timeline):23/02/2022
(Personal situation):there are three sitiuations: Great ,complete ,correct 
Complete :if the person has realized all must-have features.and there is a published GitHub repo available and the game runs until the end without any error.	
       and  game starts by running python main.py in the terminal.
Correct:if the code is well typed.	
           and there is a docstring for every function/method/class.	
           and all the constraints are respected. 
Great : if there is an interaction with the user.	
         and the game is playable with multiple users.       


--------------------------------------------------------------------------------------------

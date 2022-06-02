from hashlib import new
import random

from setuptools import SetuptoolsDeprecationWarning
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
         'Queen','King','Ace')


values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
          'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':11,'Queen':12,'King':13,'Ace':14}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    


class Deck():
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                
                #Create the Card Object
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop() 
        
class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    

#new_player = Player('tako')

#print(new_player)
    
    


#two_hearts=Card('Hearts','Two')

#three_of_clubs = Card('Clubs','Three')

#print(two_hearts)

#print(values[two_hearts.rank])

#print(three_of_clubs.value)

#print(two_hearts.value < three_of_clubs.value)



#print(new_deck.all_cards)

'''first_card= new_deck.all_cards[0]
bottom_card= new_deck.all_cards[-1]
print(first_card)
print(bottom_card)'''

'''new_deck = Deck()
new_deck.shuffle()

for card_object in new_deck.all_cards:
    print (card_object)'''
    
#GAME Setup
player_one = Player("One")
player_two = Player("Two")    

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True    
round_num = 0

while game_on:
    round_num +=1
    print(f'Round {round_num}')
    
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print ('Plater Two, out of cards!Player One Wins!')
        game_on = False
        break
    
    #Start a new Round!
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    
at_war = True

while at_war:
    
#print(len(player_one.all_cards#))

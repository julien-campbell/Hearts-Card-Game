from DecksandHands import Hand_Hearts
from CardsClass import card
class player:
  def __init__(self, name):
    self.name = name
    self.bot = False
    self.point = 0
    self.starter = False
    self.cards = Hand_Hearts(self.name)

  def play_card(self,redo):
    #Take input of what card to play
    if redo == False:
      print('which card do you like to play? You Currently have:  \n')
      for i in self.cards.cards:
        print(str(i))
    while True:
      print('\n Pick a number \n Note: Jack = 11, Queen = 12, King = 13, Ace = 14')
      user_rank = input('rank: \n')
      if user_rank.isnumeric() and int(user_rank)<=14 and int(user_rank)>=2:
        user_rank = int(user_rank)
      else:
        print('\nWrong input, must be a number between 2 and 14. Pick again!')
        continue  

      print('\n Pick a suit \nNote: Diamond = 0, Clubs = 1, Spades = 2, Hearts  = 3')
      user_suit = input('suit:  \n')
      if user_suit.isnumeric() and int(user_suit)<=4 and int(user_suit)>=0:
        user_suit = int(user_suit)
      else:
        print('\nWrong input, must be a number between 0 and 3. Pick again!')
        continue

  
      user_card = card(user_suit, user_rank) 
      if user_card in self.cards.cards:
        return user_card
      else:
        print('\nWrong card, You do not have this card! Pick again:')
     
    

class computer(player):
  def __init__(self, name):
    self.name = name
    self.bot = True
    self.point = 0
    self.starter = False
    self.cards = Hand_Hearts(self.name)
from CardsClass import card
import random
import itertools
class deck:
  def __init__(self):
    #list of deck
    self.cards = []
    #creating the cards in the deck
    for suit in range(4):
      for rank in range(2,15):
        self.cards.append(card(suit, rank))
  
  def __str__(self):
    s = ""
    for i in range(len(self.cards)):
      s = s + " " * i +str(self.cards[i])+"\n"
      
    return s
    
  def shuffle(self):
    #shuffles deck
    for i in range(len(self.cards)):
      rand = random.randint(0,len(self.cards)-1)
      temp = self.cards[i]
      self.cards[i] = self.cards[rand]
      self.cards[rand] = temp

  def deal(self, player, number_of_players):
    i=0
    while True:
      if self.cards == []:
        break
      temper = self.cards.pop()
      player[i].cards.cards.append(temper)
      i += 1
      i = i%number_of_players
  
  def remove(self,card_remove):
    self.cards.remove(card_remove)


class Hand_Hearts(deck):
  def __init__(self,name):
    self.cards = []
    self.name = name

  
  def __str__(self):
    if self.cards == []:
      return f'{self.name} has no cards!'
    else:
      a = f'{self.name} currently holds: \n'
      s = ''
      for i in range(len(self.cards)):
      
        s = s + str(self.cards[i]) + '\n'

    return a+s


  def sorts(self):
    sorter_suit = [[] for i in range(4)]

    for card_taken in self.cards: #separates by suits
        sort_card  = card_taken
        if sorter_suit[sort_card.suit] == []:
          sorter_suit[sort_card.suit].append(sort_card)
        else:
          if sorter_suit[sort_card.suit][len(sorter_suit[sort_card.suit])-1].rank <card_taken.rank: #if card rank is higher than their highest, add to the end
            sorter_suit[sort_card.suit].append(sort_card)
          else:
            for i in range(len(sorter_suit[sort_card.suit])):
              if sorter_suit[sort_card.suit][i].rank >sort_card.rank: #if card rank is lower, add there
                sorter_suit[sort_card.suit].insert(i, sort_card)
                break

    self.cards = list((itertools.chain.from_iterable(sorter_suit)))

class Hand_OldMaid(Hand_Hearts):
  def __init__(self,name):
    self.cards = []
    self.name = name
    self.bot = True
    self.point = 0
    self.starter = False
  
  def __str__(self):
    if self.cards == []:
      return f'{self.name} has no cards!'
    else:
      a = f'{self.name} currently holds: \n'
      s = ''
      for i in range(len(self.cards)):
      
        s = s + str(self.cards[i]) + '\n'

    return a+s

  def match(self):
    count = 0

    for i in self.cards:
      if card(3-i.suit,i.rank) in self.cards:
        count +=1
        
        self.cards.remove(i)
        self.cards.remove(card(3-i.suit,i.rank))

    return count
  
  def append(self, card_recieved):
    self.cards.append(card_recieved)


  def check_match(self, card_taken):
    if card(3-card_taken.suit,card_taken.rank) in self.cards:    
      self.cards.remove(card(3-card_taken.suit,card_taken.rank))
      print (f'{self.name} has taken {str(card_taken)} and made a match with {str(card(3-card_taken.suit,card_taken.rank))} \n')
      return 1
    else:
      self.cards.append(card_taken)
      print (f"{self.name} has taken {str(card_taken)}\n ")
      return 0

 
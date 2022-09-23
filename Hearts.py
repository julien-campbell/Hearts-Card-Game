from CardsClass import card
from DecksandHands import deck
import replit

class Hearts:
  def __init__(self, player):
    self.deck = deck()
    self.deck.shuffle()
    self.player = player
    self.play_hand = 0 #player x's turn to play
    self.heart_broken = False
    self.cards_per_person = 13
    self.Heart_broken_this_round = False
  def setup_hearts(self):
    if len(self.player) == 3:
      self.deck.remove(card(1,2))
      self.cards_per_person = 17
    elif len(self.player) ==5:
      self.deck.remove(card(1,2))
      self.deck.remove(card(2,2))
      self.cards_per_person = 10
    self.deck.deal(self.player, len(self.player)) #Deal cards
    print("---------- Cards have been dealt")
    for i in range(len(self.player)):
      self.player[i].cards.sorts()           #sort the cards for players based on suits then ranks
      if card(0,2) == self.player[i].cards.cards[0]:   #find player with 2 of diamond
        self.play_hand = i
        print(f'{self.player[i].name} holds the {str(card(0,2))}. He will start first:')


  def round_one_validation(self, user_card, players_cards):
    if user_card.suit == 3 or user_card == card(2,12): #Make sure hearts arn't played in first round
      print('\nWrong card, no Hearts or Queen of Spades can be played in round 1. Try again!')
      return False
    elif card(0,2) == players_cards[0]:
      if user_card != card(0,2):
        print('\nWrong card, must pick 2 of Diamonds. Try again!')
        return False
      else:
        return True
    else:
      if user_card.suit==0:
        return True
      else:
          if players_cards[0].suit ==0:
            print('\nWrong card, must play a Diamond suit card! Try Again!')
            return False
          else:
            return True


  def rounds_validation(self, user_cards, players_hand, round_suit):

    if round_suit == 10:
      if user_cards.suit == 3 and self.heart_broken == False: #Make sure hearts are only played when allowed
        print('\nWrong card, Hearts have not been broken. Try again!')
        return False
      else:
        return True
    elif round_suit == user_cards.suit:
      return True
    elif players_hand[0].suit == 3 and self.heart_broken == False:
        self.heart_broken = True
        return True

    else:
      for singlecard in players_hand: #Make sure player plays correct suit
        if round_suit == singlecard.suit:
          print('\nWrong card, must play the same suit as the first player. Try again!')
          return False
      if user_cards.suit == 3 and self.heart_broken == False:
        self.heart_broken = True
        self.Heart_broken_this_round = True

      return True





  def play_hearts(self):
    rounds = 1
    


    while rounds <= self.cards_per_person:  #play 13 rounds
      print(f'--Round {rounds} --\n')
      round_suit = 10
      loser_card = card(0,0)
      point_lost_in_round = 0
      field = [1]*len(self.player)
      most_point = 0
      announcement = ''
      #Everyone pick cards and make sure they are valid 
      for j in range(len(self.player)):   
        valid = False
        print(f'{self.player[self.play_hand].name} turn!')
        while True:
          check_player = input(f'Are you {self.player[self.play_hand].name}? (Write Y/N) \n').upper()
          if check_player == 'Y':
            replit.clear()
            print(announcement)
            break
        while valid == False:
          redo = False        
          field[self.play_hand]=self.player[self.play_hand].play_card(redo)

          if rounds ==1:
            #first card represents the player's Hand class, second represents the hand class's list
            valid = self.round_one_validation(field[self.play_hand], self.player[self.play_hand].cards.cards)
              
          else:
            valid = self.rounds_validation(field[self.play_hand], self.player[self.play_hand].cards.cards, round_suit)
        
          if valid == True:
            self.player[self.play_hand].cards.cards.remove(field[self.play_hand])
          redo = True
        if j==0:
          round_suit = field[self.play_hand].suit      
        if self.heart_broken == True and  self.Heart_broken_this_round == True:
          announcement = 'Heart is broken! \n' + announcement     
          self.Heart_broken_this_round = False           
        announcement = announcement + f'{self.player[self.play_hand].name} chose {str(field[self.play_hand])}\n'
        replit.clear()
        print(announcement) 
        self.play_hand += 1
        self.play_hand %= len(self.player)
    
      for i in range(len(field)):
        if round_suit == field[i].suit and loser_card.rank<field[i].rank:
          loser_card = field[i]
          loser = self.player[i].name
          self.play_hand = i
        if field[i].suit == 3:
          point_lost_in_round +=1
        elif field[i] == card(2,12):
          point_lost_in_round +=13
      self.player[self.play_hand].point += point_lost_in_round
      if rounds<self.cards_per_person:
        print (f'{loser} lost this round. He will go first next round')      
      rounds +=1
      final_loser = ''


    replit.clear()
    print('GAME IS OVER. SCORES:\n')
    for k in self.player:
      print(f'{k.name} : {k.point} points')
      if k.point > most_point:

        final_loser = k.name
        most_point = k.point
      elif k.point == most_point:
        losers = final_loser
        final_loser =  (f'{k.name} and {losers}')
    print(f'{final_loser} has lost the game with {most_point} points!')
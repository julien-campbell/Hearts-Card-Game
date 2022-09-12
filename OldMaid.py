from CardsClass import card
from DecksandHands import deck
from DecksandHands import Hand_OldMaid
# from UsernamesandPlayers import addbots
class oldmaid:
  def __init__(self):
    self.deck = deck()
    self.deck.shuffle()
    self.player = []
    self.matches = 0

  def setup(self, players):
    self.deck.remove(card(0,12))
    if len(players) !=4:
      number_of_bots = 4-len(players)
      players = addbots(players, number_of_bots)
    for i in range(len(players)):
      self.player.append(Hand_OldMaid(players[i]))
    self.deck.deal(self.player, len(self.player))

    print("---------- Cards have been dealt")
    for i in range(len(self.player)):
      print(str(self.player[i]))
      self.matches += self.player[i].match()   

    print("---------- Cards have been matched")
    for i in self.player:
      print(str(i))

  def play_game(self):
    turn = 0
    while self.matches <25:
      turn = turn%len(self.player)
      neighbor = (turn+1)%len(self.player)
      self.player[neighbor].shuffle()    
      temporary = self.player[neighbor].cards.pop()
      self.matches += self.player[turn].check_match(temporary)        
      if self.player[neighbor].cards == []:
        print(str(self.player[neighbor]))
        self.player.remove(self.player[neighbor])
        if turn == 0:
          continue
        else:
          turn-=1
          neighbor -=1      
      if self.player[turn].cards == []:
        print(str(self.player[turn]))
        self.player.remove(self.player[turn])
        if turn == 0:
          continue
        else:
          turn-=1
          neighbor -=1          

      

      turn +=1
    print(f"{self.player[0].name} has lost the game!")
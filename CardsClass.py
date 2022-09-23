class card: #this class creates cards including stuff like suits and numbers
  suits = ["diamonds","clubs", "spades",  "hearts"]
  ranks = ["narf", "narf", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]


  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank


    
    
  def __str__(self):
    return (self.ranks[self.rank] + " of " + self.suits[self.suit])
  
  def cmp(self, other):
  # Check the suits
    if self.suit > other.suit: return 1
    if self.suit < other.suit: return -1
    # Suits are the same... check rank
    if self.rank > other.rank: return 1
    if self.rank < other.rank: return -1
    # Ranks are the same... it's a tie
    return 0  

  def __eq__(self, other):
    return self.cmp(other) == 0

  def __le__(self, other):
      return self.cmp(other) <= 0

  def __ge__(self, other):
      return self.cmp(other) >= 0

  def __gt__(self, other):
      return self.cmp(other) > 0

  def __lt__(self, other):
      return self.cmp(other) < 0

  def __ne__(self, other):
      return self.cmp(other) != 0
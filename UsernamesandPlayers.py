from Players import player
from Players import computer

def players():
  while True:
    user_players = input('How many players? Only 3-5 players \n')
    

    
    if user_players.isnumeric() and int(user_players)<=5 and int(user_players)>=3:
      break
    else:
      print("not a valid number, please try again \n")

  Users = []
  user_players = int(user_players)
  for i in range(user_players):
    username = input(f"What is player {i+1} name?: \n")
    Users.append(player(username))
  
  # number_of_bots = 4-user_players
  # for j in range(number_of_bots):
  #   Users.append(computer(f'COM{j+1}'))
  
  return Users


# def addbots(players,Number_of_bots):
#   for i in range(Number_of_bots):
#     players.append(f'Com{i+1}')
#   return players
  
  
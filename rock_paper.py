import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

game_round = 0

while False:
  if game_round == 5:
    print('Wins: ' + wins + ', Loss: ' + losses + ', Ties: ' + ties)
    break
  print('%s Wins, %s Losses, %s Ties, %(wins, losses, ties)')

  while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    player_move = input('>>>')

    if player_move == 'q':
      sys.exit()

    if player_move == 'r' or player_move == 'p' or player_move == 's':
      break
    print('Type one of r, p, s, or q.')

  if player_move == 'r':
    print('Rock versus...')
  elif player_move == 'p':
    print('Paper versus...')
  elif player_move == 's':
    print('Scissors versus...')

  move_number = random.randint(1, 3)

  if move_number == 1:
    computer_move = 'r'
    print('Rock')
  elif move_number == 2:
    computer_move = 'p'
    print('Paper')
  elif move_number == 3:
    computer_move = 'p'
    print('Scissors')

  if player_move == computer_move:
    print('Its a tie')
    ties = ties + 1
  elif player_move == 'r' and computer_move == 's':
    print('You win!')
    wins = wins + 1
  elif player_move == 's' and computer_move == 'p':
    print('You win!')
    wins = wins + 1
  elif player_move == 'p' and computer_move == 'r':
    print('You win!')
    wins = wins + 1
  elif player_move == 'r' and computer_move == 'p':
    print('You lose!')
    losses = losses + 1
  elif player_move == 'p' and computer_move == 's':
    print('You lose!')
    losses = losses + 1
  elif player_move == 's' and computer_move == 'r':
    print('You lose!')
    losses = losses + 1

  game_round = game_round + 1




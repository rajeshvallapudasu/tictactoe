import random
def display_game_board(game_board):
  print('\n'*100)
  print("\n")
  print(game_board[1] + " | " + game_board[2] + " | " + game_board[3] + "     1 | 2 | 3")
  print("---------")
  print(game_board[4] + " | " + game_board[5] + " | " + game_board[6] + "     4 | 5 | 6")
  print("---------")
  print(game_board[7] + " | " + game_board[8] + " | " + game_board[9] + "     7 | 8 | 9")
  print("\n")

def choose_symbol():
  symbol=" "
  # choose  a symbol
  while symbol not in ["X","O"]:
    symbol=input("Player1: choose your symbol").upper()

  if symbol=="X":
    return ("X","O")
  else:
    return ("O","X")

def choose_player():
  flip=random.randint(0,1)
  if flip==0:
    return "player1"
  else:
    return "player2"
def replace_function(board,marker,position):
  board[position]=marker
def space_available(board,position):
  return board[position]==" "
def player_choice(board):
  position=0
  while position not in [1,2,3,4,5,6,7,8,9,10] or not space_available(board,position):
    position=int(input("where do you want to put your symbol"))
  return position
def is_board_full(board):
  for i in range(1,10):
    if space_available(board,i):
      return False
  return True


def win_check(board, mark):
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
          (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
          (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
          (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
          (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
          (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
          (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
          (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def replay():
  return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
  game_on = True

  player1_symbol,player2_symbol=choose_symbol()
  turn=choose_player()

  board = [" "] * 10
  while game_on:

    if turn=="player1":

      display_game_board(board)
      print(f"{turn}'s turn")
      player1_choice=player_choice(board)
      replace_function(board,player1_symbol,player1_choice)
      if win_check(board, player1_symbol):
        display_game_board(board)
        print(f'Congratulations! {turn} You have won the game!')
        game_on = False
      else:
        if is_board_full(board):
          display_game_board(board)
          print('The game is a draw!')
          break
        else:
          turn = 'player2'
    elif turn=='player2':
      display_game_board(board)
      print(f"{turn}'s turn")
      player2_choice = player_choice(board)

      replace_function(board, player2_symbol, player2_choice)
      if win_check(board, player2_symbol):
        display_game_board(board)
        print(f'Congratulations! {turn} You have won the game!')
        game_on = False
      else:
        if is_board_full(board):
          display_game_board(board)
          print('The game is a draw!')
          break
        else:
          turn = 'player1'
  if not replay():
    break
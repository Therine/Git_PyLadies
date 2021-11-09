from random import randrange
player_mark = input("Hi! Let's play a nice game of tic-tac-toe. Or maybe in our case, let's just call it tic, because we are only playing in one dimension. Anyway, would you like to be an X or O? ")
if player_mark = "X" or "x":
  pc_mark = "O"
else: 
  pc_mark = "X"
#Step 1
#Write a function evaluate that gets the string with the board of 1D tic-tac-toe, and returns one character based on the state of the game:
board = -*20
def evaluate(board)
    if board == "%xxx%"
        return "X"
    elif board == "%ooo%"
        return "O"
    elif board != "-"
        return "!"
    else
        return "-"  


#"!" – Draw (the board is full but nobody has won)
#"-" – Rest (i.e. the game is not finished)
#Step 2
#Write a move function that gets the string with the game board, a position number (0-19), and a (x or o) mark, and returns a game board (i.e., a string with the given mark placed in the given position). The function header should look something like this:

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    print(board)
#Step 3
#Write a player_move function that gets a string with the game board, asks the player which position he wants to play, and returns the updated game board with the player's move. The function should reject negative or too large numbers or moves to an occupied position. If the user has entered a wrong argument, the function should ask again (to get correct answer).
def player_move(position)
  position = int(input("Where you would like to place your piece (0-19)? "))
  chosen_position = position[position]
  if chosen_position == '-':
    # somehow replace this dash with the player_marker. I think that this is going to involve a for loop
    for i in range (19)
      if position[i] == '-'
        break
      elif position[]
  else:
    print("Sorry, my friend, that position is already taken!")

#Step 4
#Write a pc_move function that gets the string with the game board. It will select a position to play, and returns the game board with the computer's move.
#Use a simple random "strategy":
def pc_move(position)
  position = randrange(19)

#Select a random number from 0 to 19.
#If the position is empty, place the computer's mark there.
#If not, repeat from the first step (select another random number). The function header should look something like this:
def pc_move(board):
    # Returns a game board with the computer's move.
    ...
#Step 5
#Write a 1D_tictactoe function that creates a string with a game board and alternately calls the player_move and pc_move functions until someone wins or draws. Do not forget to check the status of the game after every turn.

#Step 6 - Optional
#Can you think of better strategy for your computer? Let us know your ideas or try to program them directly.
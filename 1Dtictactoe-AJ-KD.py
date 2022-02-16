from random import randrange
player_mark = input("Hi! Let's play a nice game of tic-tac-toe. Or maybe in our case, \n let's just call it tic, because we are only playing in one dimension. \n Anyway, would you like to be an X or O? ")

def assign_mark(player_mark):  
  if player_mark == "X" or "x":
    assign_mark.pc_mark = "o"
    assign_mark.player_mark = "x"
  elif player_mark == "0" or "o" or "O":
    assign_mark.pc_mark = "x"
    assign_mark.player_mark = "o"
  return assign_mark.pc_mark, assign_mark.player_mark
print(assign_mark(player_mark))

#Step 1
#Write a function evaluate that gets the string with the board of 1D tic-tac-toe, and returns one character based on the state of the game:
def evaluate(board):
    if board == "%xxx%":
        return "X"
    elif board == "%ooo%":
        return "O"
    elif board != "-":
        return "!"
    else:
        return "-"  


#"!" – Draw (the board is full but nobody has won)
#"-" – Rest (i.e. the game is not finished)
#Step 2
#Write a move function that gets the string with the game board, a position number (0-19), and a (x or o) mark, and returns a game board (i.e., a string with the given mark placed in the given position). The function header should look something like this:

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    board = '-'*20 #this should be an official list like board = ['- '*20]?
    print ("Let's take a look at the board, shall we?")
    print(board)
    print("Right, that line of dashes is our board. As you play, the board should update \n with your marker and then the computer's marker until one of you get 3 in a row.")
    goes_first = input("So, which one of you should go first, you or the computer. Type in 'me' or 'pc': ")
    if goes_first == "me":
        player_move(position = int(input("Where you would like to place your piece (0-19)? ")))

#Step 3
#Write a player_move function that gets a string with the game board, asks the player which position he wants to play, and returns the updated game board with the player's move. The function should reject negative or too large numbers or moves to an occupied position. If the user has entered a wrong argument, the function should ask again (to get correct answer).
#this function needs work. 
def player_move(position):
  position = int(input("Where you would like to place your piece (0-19)? "))
  chosen_position = position[position]
  if chosen_position == '-':
    # somehow replace this dash with the player_marker. I think that this is going to involve a for loop
    for i in range (19):
      if position[i] == '-':
        break
      else:
        position[player_mark]

  else:
    print("Sorry, my friend, that position is already taken!")
  print(board)

#Step 4
#Write a pc_move function that gets the =string with the game board. It will select a position to play, and returns the game board with the computer's move.
#Use a simple random "strategy":
def pc_move(position):
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
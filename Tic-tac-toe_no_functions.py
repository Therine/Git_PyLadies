# 1. Introduce the game. 
# 2. Find out which mark the human wants to use.
# 3. Assign the other mark to the computer.
# 4. Display the tic-tac-toe board empty with 20 dashes.
# 5. Find out who should go first.
# 6. If it is the human, ask them where they want to place their marker. 
# 7. Update the board with the mark in the that place.
# 8. If it is the computer, run the random number generater between 0-19. 
# 9. Display the board with the new marker.
# 10. Next move and all future moves. 
# 11. Alternate players
# 12. Ask the player (run the random generator) for a position number.
# 13. If the position is a dash, place the mark.
# 14. If the position is a mark, display that the position is already filled and the player needs to pick a new position number. 
# 15. After each mark is added, check to see if the board has any xxx or ooo in the string.
# 16. Once there is an xxx or an ooo, announce that the player with that mark won and ask if they want to play again. Restart at the beginning if yes and exit game if not.
board = "--------------------"
print("Let's play a nice game of tic-tac-toe,\nerr maybe it is really just tic?\nThere is only one dimension of 20 positions, and it looks like this\n", board )
player_mark_input = input("Anyway, would you like to be an x or o? ")
# Trying to learn how use the variables pc_mark and player_mark outside of this assign_mark function.
# https://www.kite.com/python/answers/how-to-access-a-variable-outside-of-a-function-in-python
# 

def assign_mark(player_mark_input):  
  if player_mark_input == "X" or "x":
    pc_mark = "o"
    player_mark = "x"
  elif player_mark_input == "0" or "o" or "O":
    pc_mark = "x"
    player_mark = "o"
  return (pc_mark, player_mark)
print("Great, you'll be", assign_mark(player_mark_input)[1], "and I'll be", assign_mark(player_mark_input)[0])
goes_first = input("So, which one of you should go first, you or the computer. Type in 'me' or 'pc': ")
if goes_first == 'me':
    position = int(input("Pick a number between 0 and 19: "))
    if board[position] == "-":  
      temp = list(board)
      temp[position] = assign_mark(player_mark_input)[1]
      board = "".join(temp)
    else:
      print("There is already a mark at that spot.")
      
print(board)




    
    
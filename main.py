# Griffin King
# Unit 2 Lab 3
# making Tic Tac Toe
import os
from tic_tac_toe import TicTacToe
from time import sleep
def storage():
  winner = True
  turns = 0
  game = TicTacToe()
  return winner, turns, game

def checker(user):
  if user in ["1","2","3"]:
    return True
def main():
  
  winner, turns, game = storage()
  input("\n<>-----------------------------------\n\n  Welcome to Tic-Tac-Toe\n\n  X and O will be initially randomly assigned,\n  Press Enter When Ready\n\n  ")

  while winner and turns < 9:
    
    os.system("clear")
    print("\n<>-----------------------------------\n\n  Welcome to Tic-Tac-Toe\n  Please select a spot to place your token,\n")
    print(game)
    userInput1 = input("  Select a row (1-3)")

    if checker(userInput1):
      userInput2 = input("  Select a column (1-3)")
      
      
      if checker(userInput2):
        flag = game.place_token(userInput1,userInput2)
        
        
        if flag == True:
          sleep(0.2)
          winner, tokenWon = game.is_winner()
          turns += 1
        else:
          input("\n  A token is already at that location, please try again!")
      
      
      else:
        input("\n  Incorrect Input!")
    else:
      input("\n  Incorrect Input!")
  
  
  if turns == 9:
    print("\n  Game has resulted in a draw!")
  else:
    print(f"\n  {tokenWon} has won the game!\n")



if __name__ == "__main__":
  os.system("clear")
  main()
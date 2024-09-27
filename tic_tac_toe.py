from random import randint
class TicTacToe:
  def __init__(self):
    
    self.__turn = ['X','O'][randint(0,1)]
    self.__board = [[" " for b in range(3)] for a in range(3)]

  def __check_win(self, token):
    #Top left
    if self.__board[0][0] == token:
      if self.__board[0][1] == token:
        if self.__board[0][2] == token:
          return False
      elif self.__board[1][1] == token:
        if self.__board[2][2] == token:
          return False
      elif self.__board[1][0] == token:
        if self.__board[2][0] == token:
          return False

    #Top right
    elif self.__board[0][2] == token:
      if self.__board[1][2] == token:
        if self.__board[2][2] == token:
          return False
      elif self.__board[1][1] == token:
        if self.__board[2][0] == token:
          return False

    #Top middle
    elif self.__board[0][1] == token:
      if self.__board[1][1] == token:
        if self.__board[2][1] == token:
          return False
    
    #Middle left
    elif self.__board[1][0] == token:
      if self.__board[1][1] == token:
        if self.__board[1][2] == token:
          return False
    
    #Bottom left
    elif self.__board[2][0] == token:
      if self.__board[2][1] == token:
        if self.__board[2][2] == token:
          return False
    else:
      return True


  def place_token(self, userInput1, userInput2):
    if self.__board[int(userInput1)-1][int(userInput2)-1] == " ":
      self.__board[int(userInput1)-1][int(userInput2)-1] = self.__turn
      if self.__turn == 'X':
        self.__turn = 'O'
      else:
        self.__turn = 'X'
      return True
    else:
      return False


  def is_winner(self):
    for a in ['X','O']:
      Win = self.__check_win(a)
      if Win == False:
        return Win, a
    return True, "Sean is a bozo"


  def __str__(self):
    return "  @-1--2--3-\n"+"  1 "+str(self.__board[0][0])+"| "+str(self.__board[0][1])+" |"+str(self.__board[0][2])+"\n  |---------\n  2 "+ str(self.__board[1][0])+"| "+str(self.__board[1][1])+" |"+str(self.__board[1][2])+"\n  |---------\n  3 "+str(self.__board[2][0])+"| "+str(self.__board[2][1])+" |"+str(self.__board[2][2]+"\n")
    
   #\\ //   //=\\
   # >X<    || ||
   #// \\   \\=//



  
  #        __       __
  #        ||       ||
  #        ||       ||
  #        ||       ||
  # |======@@=======@@======|
  #        ||       ||
  #        ||       ||
  #        ||       ||
  #        ||       ||
  # |======@@=======@@=======|
  #        ||       ||
  #        ||       ||
  #        ||       ||
  #        --       --
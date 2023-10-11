import string, random

class BoggleBoard:
  def __init__(self, dice):
    self._board = ["______" for num in range(0, dice)]
    self.get_board
    self._dice = dice
  
  @property
  def get_board(self):
    for group in self._board:
      print(f"{group}\n")

  
  def shake(self):
    for idx in range(0, len(self._board)):
      rando = ''.join(random.choices(string.ascii_uppercase, k=6))
      self._board[idx] = rando
    self.get_board

new_board = BoggleBoard(16)
new_board.shake()

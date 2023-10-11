import string, random

class BoggleBoard:
  n = 4

  def __init__(self):
    self._board = ["____", "____", "____", "____"]
    self.get_board
  
  @property
  def get_board(self):
    for group in self._board:
      print(f"{group}\n")

  
  def shake(self):
    for idx in range(0, len(self._board)):
      rando = ''.join(random.choices(string.ascii_uppercase, k=4))
      self._board[idx] = rando
    self.get_board

new_board = BoggleBoard()
new_board.shake()
new_board.shake()
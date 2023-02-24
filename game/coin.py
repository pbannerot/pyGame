import random
from enum import Enum

class Side (Enum):
  HEADS = 0
  TAILS = 3

class Coin:
  def __init__ (self):
    self.roll()
  
  def __repr__ (self):
    return self._side.name

  def __lt__ (self, other):
    return self._side.value < other._side.value

  @property
  def value (self):
    return self._side.value

  def roll (self):
    self._side = random.choice ((Side.TAILS, Side.HEADS))


class UserStory:
  def __init__ (self):
    coin = Coin()
    for n in range (5):
      print(f"{coin} : {coin.value}")
      coin.roll()


if __name__ == "__main__":
  UserStory()


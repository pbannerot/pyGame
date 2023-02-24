from game.die import Die
from game.coin import Coin
from game.cup import Cup


class Player:
  def __init__ (self, *, name):
    if name.isspace() or len (name) == 0:
      raise ValueError ("invalid player name")
    self._name = name
    self._score = 0

  def takeTurn (self, *, rollable):
    rollable.roll()
    self._score += rollable.value
    print (f"{self} got {rollable.value} points {rollable}")

  def __lt__ (self, other):
    if self.score == other.score:
      return other.name < self.name
    return self.score < other.score

  def __repr__ (self):
    return self._name

  @property
  def score (self):
    return self._score


import unittest

class PlayerTest (unittest.TestCase):
  PLAYER_NAME = "Sitting Bull"

  def test_ctor_with_an_empty_name_must_fail (self):
    with self.assertRaises (Exception):
      Player ("")

  def test_ctor_with_a_blank_name_must_fail (self):
    with self.assertRaises (Exception):
      Player ("    ")

  def test_ctor_score_is_zero (self):
    self.assertEqual (Player(name = PlayerTest.PLAYER_NAME).score, 0)

  def test_ctor_name_is_set (self):
    player = Player (name = PlayerTest.PLAYER_NAME)
    self.assertEqual (PlayerTest.PLAYER_NAME, str(player))

  def test_take_turn_increases_the_score(self):
    player = Player (name = PlayerTest.PLAYER_NAME)
    cup = Cup (rollable_type = Die, nb_rollables = Cup.MIN_NB_ROLLABLES)
    player.takeTurn (rollable = cup)
    self.assertEqual (cup.value, player.score)

  def test_lt (self):
    player1 = Player (name = PlayerTest.PLAYER_NAME)
    player2 = Player (name = PlayerTest.PLAYER_NAME)
    player1.takeTurn (rollable = Cup(rollable_type = Die, nb_rollables = Cup.MAX_NB_ROLLABLES))
    self.assertTrue (player2 < player1)

  def test_score_is_invariant (self):
    player = Player (name = PlayerTest.PLAYER_NAME)
    self.assertEqual (player.score, player.score)

class UserStory:
  def __init__ (self):
    cup = Cup (rollable_type = Coin, nb_rollables = Cup.MAX_NB_ROLLABLES)
    player = Player (name = "Sitting Bull")
    print (f"{player} has {player.score} points")
    player.takeTurn (rollable = cup)
    print (f"{player} has {player.score} points")


if __name__ == "__main__":
  #unittest.main()
  UserStory()

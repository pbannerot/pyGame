from game.die import Die
from game.coin import Coin

class Cup:
  MIN_NB_ROLLABLES = 1
  MAX_NB_ROLLABLES = 10

  def __init__ (self, rollable_type, nb_rollables):
    if nb_rollables < Cup.MIN_NB_ROLLABLES or nb_rollables > Cup.MAX_NB_ROLLABLES:
      raise ValueError ("invalid number of dice")

    self._rollables = tuple (rollable_type() for x in range (nb_rollables))
    self._value = None

  def __repr__ (self):
    s = "["
    for rollable in sorted (self._rollables):
      s = f"{s} {rollable}"
    s = f"{s} ]"
    return s

  def roll (self):
    for rollable in self._rollables:
      rollable.roll()
    self._value = None

  @property
  def value(self):
    if not self._value:
      self._value = 0
      for rollable in self._rollables:
        self._value += rollable.value
    return self._value


import unittest

class CupTest (unittest.TestCase):

  def test_construction_with_too_few_rollables_must_fail (self):
    with self.assertRaises (Exception):
      Cup(rollable_type = Die, nb_rollables = Cup.MIN_NB_ROLLABLES - 1)

  def test_construction_with_too_many_rollables_must_fail (self):
    with self.assertRaises (Exception):
      Cup(rollable_type = Die, nb_rollables = Cup.MAX_NB_ROLLABLES + 1)

  def test_repr_is_enclosed_in_brackets (self):
    s = str(Cup (rollable_type = Die, nb_rollables = Cup.MIN_NB_ROLLABLES))
    self.assertTrue (s.startswith ("[ ") and s.endswith (" ]"))


class DieCupTest (unittest.TestCase):

  def setUp (self):
    self.cup = Cup (rollable_type = Die, nb_rollables = Cup.MAX_NB_ROLLABLES)

  def test_repr_len_depends_on_nb_rollables (self):
    s = str(self.cup)
    self.assertEqual (len (s), Cup.MAX_NB_ROLLABLES * 2 + len ("[ ]"))

  def test_getValue_is_ge_nb_rollables(self):
    self.assertTrue (self.cup.value >= Cup.MAX_NB_ROLLABLES)


class UserStory:
  def __init__ (self):
    cup = Cup (rollable_type = Coin, nb_rollables = 5)
    print (cup)

if __name__ == "__main__":
  unittest.main()
  #UserStory()

import random

class Die:

  MIN_VALUE = 1
  MAX_VALUE = 6

  def __init__ (self):
    self.roll()
  
  def __repr__ (self):
    return str (self._faceValue)

  def __lt__ (self, other):
    return self._faceValue < other._faceValue

  @property
  def value (self):
    return self._faceValue

  def roll (self):
    self._faceValue = random.randint (1, 6)

import unittest

class DieTest (unittest.TestCase):

  def _assertIntegrity (self, die):
    self.assertTrue (die.value >= Die.MIN_VALUE and die.value <= Die.MAX_VALUE)    

  def setUp (self):
    self.die = Die()

  def test_constructor_integrity (self):
    self._assertIntegrity (self.die)
    
  def test_value_is_invariant (self):
    self.assertEqual (self.die.value, self.die.value)

  def test_roll_integrity (self):
    self.die.roll()
    self._assertIntegrity (self.die)

  def test_str_len_is_one (self):
    self.assertEqual (len (repr (self.die.value)), 1)

  def test_str_returns_the_value (self):
    self.assertEqual (self.die.value, int (str(self.die)))


class DieCoverageTest (unittest.TestCase):
  NB_LOOPS = 30
    
  def setUp (self):
    self.values = set()

  def tearDown (self):
    self.assertEqual (Die.MAX_VALUE, len (self.values))
    for n in range (Die.MIN_VALUE, Die.MAX_VALUE + 1):
      self.assertTrue (n in self.values)
    
  def test_constructor_coverage (self):
    for n in range (DieCoverageTest.NB_LOOPS):
      self.values.add (Die().value)      

  def test_roll_coverage (self):
    die = Die()
    for n in range (DieCoverageTest.NB_LOOPS):
      die.roll()
      self.values.add (die.value)      


class UserStory:
  def __init__ (self):
    d = Die()
    for n in range (5):
      print(d)
      d.roll()


if __name__ == "__main__":
  #unittest.main()
  UserStory()

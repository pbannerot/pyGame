from game.coin import Coin
from game.die import Die
from game.cup import Cup
from game.player import Player


class Game:
  MIN_NB_TURNS = 1
  MAX_NB_TURNS = 10
  MIN_NB_PLAYERS = 2
  MAX_NB_PLAYERS = 8

  def _setup_done(self):
    return self._nb_turns and self._cup

  def _play_turn (self, turn):
    print (f"\nturn #{turn}")
    for player in self._players.values():
      player.takeTurn (rollable=self._cup)

  def _save_scores (self):
    with open("C:\\Users\\Artworks\\Desktop\\scores.txt", "w") as f:
      for player in self._players.values():
        f.write(f"{player} {player.score}\n")

  def __init__ (self):
    self._players = {}
    self._nb_turns = None
    self._cup = None

  def _display_winner (self):
    winner = max (self._players.values())
    print (f"\n{winner} won with {winner.score} points")

  def setup(self, rollable_type, nb_rollables, nb_turns):
    self._cup = Cup (rollable_type, nb_rollables)
    if nb_turns < Game.MIN_NB_TURNS or nb_turns > Game.MAX_NB_TURNS:
      raise ValueError ("invalid number of turns")
    self._nb_turns = nb_turns

  def register(self, player_name):
    if player_name in self._players:
      raise Exception (f"{player_name} is already registered")
    if len (self._players) == Game.MAX_NB_PLAYERS:
      raise Exception ("too many players are registered")
    self._players[player_name] = Player (name=player_name)

  def start(self):
    if not self._setup_done():
      raise Exception ("setup is not done")
    if len (self._players) < Game.MIN_NB_PLAYERS:
      raise Exception ("too few players are registered")

    print ("WELCOME TO LAS VEGAS")
    for turn in range (1, self._nb_turns + 1):
      self._play_turn (turn)
    self._display_winner()
    self._save_scores()


import unittest


class GameTest (unittest.TestCase):
  PLAYER_NAME = "Sitting Bull"

  def setUp (self):
    self.game = Game()

  def test_setup_with_too_few_dice_must_fail (self):
    with self.assertRaises (Exception):
      self.game.setup (Cup.MIN_NB_ROLLABLES - 1, Game.MIN_NB_TURNS)

  def test_setup_with_too_many_dice_must_fail (self):
    with self.assertRaises (Exception):
      self.game.setup (Cup.MAX_NB_ROLLABLES + 1, Game.MIN_NB_TURNS)

  def test_setup_with_too_few_turns_must_fail (self):
    with self.assertRaises (Exception):
      self.game.setup (Cup.MIN_NB_ROLLABLES, Game.MIN_NB_TURNS - 1)

  def test_setup_with_too_many_turns_must_fail (self):
    with self.assertRaises (Exception):
      self.game.setup (Cup.MIN_NB_ROLLABLES, Game.MAX_NB_TURNS + 1)

  def test_register_an_empty_name_must_fail (self):
    with self.assertRaises (Exception):
      self.game.register ("")

  def test_register_a_blank_name_must_fail (self):
    with self.assertRaises (Exception):
      self.game.register ("    ")

  def test_register_twice_the_same_player_must_fail (self):
    self.game.register (GameTest.PLAYER_NAME)
    with self.assertRaises (Exception):
      self.game.register (GameTest.PLAYER_NAME)

  def test_register_too_many_players_must_fail (self):
    for n in range (Game.MAX_NB_PLAYERS):
      self.game.register (GameTest.PLAYER_NAME + str(n))
    with self.assertRaises (Exception):
      self.game.register (GameTest.PLAYER_NAME)

  def test_start_without_setup_must_fail (self):
    self._registerPlayers (Game.MIN_NB_PLAYERS)
    with self.assertRaises (Exception):
      self.game.start()

  def test_start_with_too_few_players_must_fail (self):
    self.game.setup (Die, Cup.MIN_NB_ROLLABLES, Game.MIN_NB_TURNS)
    self._registerPlayers (Game.MIN_NB_PLAYERS - 1)
    with self.assertRaises (Exception):
      self.game.start()

  def _registerPlayers (self, nb_players):
    for n in range (nb_players):
      self.game.register (f"GameTest.PLAYER_NAME{n}")


class UserStory:

  def __init__ (self):
    g = Game()
    g.setup (rollable_type=Coin, nb_rollables=6, nb_turns=4)
    g.register (player_name="Sitting Bull")
    g.register (player_name="Geronimo")
    g.start()


if __name__ == "__main__":
  # unittest.main()
  UserStory()

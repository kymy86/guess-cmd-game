"""
Test suite for the guess game
"""
import unittest
from guesser import Guesser

class DifficultyTest(unittest.TestCase):
    """
    Unit test for difficulties
    """

    @classmethod
    def setUpClass(cls):
        cls.guesser = Guesser()

    def test_difficulty_in_range(self):
        """ Test the right difficulty levels"""
        for i in ["1", "2", "3"]:
            with self.subTest(i=i):
                res = self.guesser.choose_challenge_level(i)
                self.assertTrue(res)

    def test_difficulty_forbidden_value(self):
        """ Forbidden values must not be accepted"""
        for i in ["test", None, "", "test", "4"]:
            with self.subTest(i=i):
                res = self.guesser.choose_challenge_level(i)
                self.assertFalse(res)


    def test_game_forbidden_guesses(self):
        """ Forbidden guesses must not be accepted"""
        self.guesser.difficulty = 1
        for i in ["", None]:
            with self.subTest(i=i):
                res = self.guesser.run_game(i, 1)
                self.assertFalse(res)
                self.assertEqual(self.guesser.status, -100)

    def test_game_attempts(self):
        """ If attempts are greater than allows, return false"""
        for key in self.guesser.difficult_dict.keys():
            with self.subTest(key=key):
                self.guesser.difficulty = key
                res = self.guesser.run_game(12, 11)
                self.assertFalse(res)
                self.assertEqual(self.guesser.status, -100)

class RunGameTest(unittest.TestCase):
    """
    Unit test for game mechanics
    """
    @classmethod
    def setUpClass(cls):
        cls.guesser = Guesser()

    def setUp(self):
        self.guesser.difficulty = 3
        self.guesser.guess_number = 5

    def test_game_guess_small(self):
        """ if user guess is small than system one, return -1"""
        res = self.guesser.run_game(3, 1)
        self.assertTrue(res)
        self.assertEqual(self.guesser.status, -1)

    def test_game_guess_big(self):
        """ if user guess is greater than the system one, return 1"""
        res = self.guesser.run_game(10, 1)
        self.assertTrue(res)
        self.assertEqual(self.guesser.status, 1)

    def test_game_guess_ok(self):
        """ if user guess is equal than the system one, return 0"""
        res = self.guesser.run_game(5, 1)
        self.assertFalse(res)
        self.assertEqual(self.guesser.status, 0)


if __name__ == '__main__':
    unittest.main()












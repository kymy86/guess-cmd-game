"""
Manage the number guess
"""
import random

class Guesser:
    difficultDict = {
        1:10,
        2:6,
        3:2,
    }
    minRange = 1
    maxRange = 20
    _INIT_STATUS = -100

    def __init__(self):
        self.difficulty = 0
        self.status = self._INIT_STATUS
        self.generate_number()

    def generate_number(self):
        """ generate a random number for the user """
        self.guess_number = random.randrange(Guesser.minRange, Guesser.maxRange)

    def choose_challenge_level(self, difficulty):
        """ check if the difficulty value is valid or not """

        difficulty = self.__check_valid_value(difficulty)
        if not difficulty:
            return False

        if difficulty not in Guesser.difficultDict.keys():
            return False
        else:
            self.difficulty = difficulty
            return True

    def run_game(self, user_guess, count):
        """ Check if player wins or loses"""
        if count >= self.get_number_of_attempts():
            self.status = self._INIT_STATUS
            return False

        user_guess = self.__check_valid_value(user_guess)
        if not user_guess:
            self.status = self._INIT_STATUS
            return False

        if user_guess == self.guess_number:
            self.status = 0
            return False
        if user_guess < self.guess_number:
            self.status = -1
            return True
        if user_guess > self.guess_number:
            self.status = 1
            return True

    def __check_valid_value(self, value):
        try:
            return int(value)
        except ValueError:
            return False
        except TypeError:
            return False

    @staticmethod
    def get_min_difficulty():
        """ Return the minimum value of the game level challenge """
        return min(Guesser.difficultDict.keys(), key=int)

    @staticmethod
    def get_max_difficulty():
        """ Return the maximum value of the game level chanllenge"""
        return max(Guesser.difficultDict.keys(), key=int)

    def get_number_of_attempts(self):
        """ Return the number of attempts for the given difficulty"""

        return Guesser.difficultDict[self.difficulty]

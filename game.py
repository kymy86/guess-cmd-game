"""
Simple guess game
"""
#!/usr/bin/python3
#pylint: disable=C0103
from guesser import Guesser

def create_guess_game():
    """ Define game logic"""
    your_name = input("Hello! What's your name?\n")
    guesser = Guesser()
    maxD = Guesser.get_max_difficulty()
    minD = Guesser.get_min_difficulty()
    guess = False

    while guess is False:
        difficulty = input("{}, choose a difficulty between {} and {}  ".format(
            your_name,
            minD,
            maxD))
        guess = guesser.choose_challenge_level(difficulty)

    print('Well, {} I am thinking of a number between {} and {}'.format(
        your_name,
        Guesser.minRange,
        Guesser.maxRange))

    run = True
    count = 0

    while run is True:
        user_guess = input("{}, take a guess:   ".format(your_name))
        count += 1
        run = guesser.run_game(user_guess, count)
        if guesser.status == -1:
            print("Your guess is too low\n")
        if guesser.status == 1:
            print("Your guess is too high\n")

    if guesser.status == 0:
        print("Good Job {} You guessed my number in {} guesses!".format(your_name, count))
    else:
        print("{}, you've lost. My number was {}".format(your_name, guesser.guess_number))


if __name__ == '__main__':
    create_guess_game()

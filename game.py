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
        difficulty = input("%s, choose a difficulty between %d and %d\n" % (your_name, minD, maxD))
        guess = guesser.choose_challenge_level(difficulty)

    print('Well, %s I am thinking of a number between %d and %d\n' % (your_name, Guesser.minRange, Guesser.maxRange))

    run = True
    count = 0

    while run is True:
        user_guess = input("%s, take a guess\n" % (your_name))
        count += 1
        run = guesser.run_game(user_guess, count)
        if guesser.status == -1:
            print("Your guess is too low\n")
        if guesser.status == 1:
            print("Your guess is too high\n")

    if guesser.status == 0:
        print("Good Job %s You guessed my number in %d guesses!" % (your_name, count))
    else:
        print("%s, you've lost. My number was %d" % (your_name, guesser.guess_number))


if __name__ == '__main__':
    create_guess_game()

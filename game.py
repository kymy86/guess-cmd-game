"""
Simple guess game
"""
from guesser import Guesser

def create_guess_game():
    """ Define game logic"""
    your_name = input("Hello! What's your name?\n")
    guesser = Guesser()
    maxD = Guesser.get_max_difficulty()
    minD = Guesser.get_min_difficulty()
    guess = False

    while not guess :
        difficulty = input(f"{your_name}, choose a difficulty between {minD} and {maxD}  ")
        guess = guesser.choose_challenge_level(difficulty)
        print(f'Well, {your_name} I am thinking of a number between {Guesser.minRange} and {Guesser.maxRange}')

    run = True
    count = 0

    while run:
        user_guess = input(f"{your_name}, take a guess:   ")
        count += 1
        run = guesser.run_game(user_guess, count)
        if guesser.status == -1:
            print("Your guess is too low\n")
        if guesser.status == 1:
            print("Your guess is too high\n")

    if guesser.status == 0:
        print(f"Good Job {your_name} You guessed my number in {count} guesses!")
    else:
        print(f"{your_name}, you've lost. My number was {guesser.guess_number}")


if __name__ == '__main__':
    create_guess_game()

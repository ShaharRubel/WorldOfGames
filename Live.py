import GuessGame as GG
import MemoryGame as MG
import CurrencyRouletteGame as CRG
import Score as score

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("\t 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("\t 2. Guess Game - guess a number and see if you chose like the computer")
    print("\t 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    # init valid entries for games 1 to 3, init game to be 0
    games = [1,2,3]
    game = 0
    # init difficulty options 1 to 5
    difficulties = [1,2,3,4,5]
    difficulty = 0
    # check for valid entry: between 1-3 and is a valid number
    while game not in games:
        try:
            game = int(input("Please select game: "))
        except:
            print("invalid entry please enter a valid number between 1 to 3")

    # check for valid entry: between 1-5 and is a valid number
    while difficulty not in difficulties:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        except:
            print("invalid entry please enter a valid number between 1 to 5")

    # Game choice logic
    result = False
    if game == 1:
        result = MG.play(difficulty)
    elif game == 2:
        result = GG.play(difficulty)
    elif game == 3:
        result = CRG.play(difficulty)
    else:
        print("you managed to cheat the system, this variable has been validated before")

    # result logic
    if result:
        print("You Won! Congrats!")
        score.add_score(difficulty)
    else:
        print("You lost, Better luck next time!")
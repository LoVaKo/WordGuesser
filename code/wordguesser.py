'''
Main function for commandline-based wordguesser game. 

main() displays a menu to the player with three options:
1. Start a new game
2. Print high score
3. Quit

The programming keeps running untill the player quits.
'''

from game import Game
from player import Player
from highscore_utils import print_highscore, add_player_score

def main():
    menu = ("WELCOME TO WORDGUESSER"       "\n"
            "1. New game"                  "\n"
            "2. Print highscore"           "\n"
            "3. Quit"                      "\n")

    while True:
        user_input = input(menu)
        match user_input:
            case "1": 
                name = input("What is your name?\n")
                player = Player(name)
                game = Game(player)
                game.start()
                add_player_score(game.player_score)
            case "2":
                print_highscore()
            case "3": 
                print("Thank you for playing!")
                return
            case _:
                print("Invalid input. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
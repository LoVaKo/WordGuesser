'''
Game module for wordguesser.

Class Game: 
    - Initialized with Player instance.
    - Level is picked by the player at the start of the game.
    - The game runs for 10 rounds.
    - After 10 rounds have been played the player's score is stored.

Functions:
    - __init__(self, player): Initializes new game for given player.
    - pick_level(self): Allows the player to pick a difficulty level.
    - display_round_info(self): Prints round information.
    - set_player_score(self, player_score): Stores player score after 
      all rounds have been completed.
    - start(self): Begins the game loop, runs for 10 rounds and 
      initializes the wrap up. 
'''
from round import Round

class Game:
    
    def __init__(self, player):
        self.player = player
        self.level = None
        self.rounds = 10
        self.player_score = None
    
    def pick_level(self):
        print(f"\nWelcome, {self.player.name}!")
        try:
            user_input = input(
                "Please pick a difficulty level by entering the corresponding "
                "number:"                   "\n"
                "1. Beginner (7 guesses)"   "\n"                                                
                "2. Easy (6 guesses)"       "\n"
                "3. Medium (5 guesses)"     "\n"
                "4. Hard (4 guesses)"       "\n"
                "5. Expert (3 guesses)"     "\n"
                )
            
            if user_input not in ("1", "2", "3", "4", "5"):
                raise ValueError
            match user_input:
                case "1": self.level = self.player.level = "Beginner"
                case "2": self.level = self.player.level = "Easy"
                case "3": self.level = self.player.level = "Medium"
                case "4": self.level = self.player.level = "Hard"
                case "5": self.level = self.player.level = "Expert"
                
        except ValueError:
            print("Invalid input. Please pick a number from 1 to 5.")

    def display_round_info(self):
        print(                                               "\n"
                f"LEVEL:            {self.level} "           "\n"
                f"POINTS:           {self.player.points}"    "\n"
                f"FAILS:            {self.player.fails}"     "\n"
                f"REMAINING ROUNDS: {self.rounds}"           "\n")
        
    def set_player_score(self, player_score):
        self.player_score = player_score

    def start(self):
        self.pick_level()

        while self.rounds > 0:
            self.display_round_info()
            new_round = Round(self.player, self.level)
            new_round.start()
            self.rounds -= 1
        
        player_score = self.player.wrap_up()
        self.set_player_score(player_score)



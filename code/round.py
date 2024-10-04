'''
Round module for wordguesser.

class Round:
    - Initialized with player and level
    - Tries are set at the start of the round
    - The round ends when:
        - Number of tries reaches zero.
        - All letters of the word have been guessed.
    - When the round ends the player stats are updated.

Functions:
    - set_random_word(): Static method that picks a random 7 character word.
    - __init__(self, player, level): Initializes a new round.
    - set_tries(self): Sets number of tries matching the level.
    - pick_letter(self): Prompts the player to pick a letter.
    - print_round_information(self): Displays round information to the player.
    - check_for_end(self): Checks for end of round conditions.
    - update(self, guess): Updates the gameboard or number of tries.
    - start(self): Runs the game loop for the current round.
    '''
import random as rd

class Round:

    @staticmethod
    def set_random_word():
        possible_words = [
            "abandon", "baggage", "cabinet", "dancing", "passion",
            "fantasy", "giraffe", "harmony", "imagery", "jackets",
            "kitchen", "languid", "magical", "narrate", "octopus",
            "package", "quizzes", "rainbow", "diamond", "example",
            "unicorn", "victory", "writers", "xylitol", "yawning",
            "zealous", "ability", "bizarre", "courage", "decline",
            "exhibit", "factors", "genuine", "heavens", "improve",
            "journey", "kingdom", "ladders", "mystery", "nostalg",
            "optimal", "precise", "qualify", "respect", "stamina",
            "triumph", "upwards", "vintage", "whisper", "xylomas",
            "yankees", "zephyrs", "artwork", "brother", "curious",
            "dormant", "elevate", "fragile", "glimpse", "hustler",
            "insight", "justice", "kitchen", "lighten", "modesty",
            "neither", "opinion", "puzzles", "quantum", "remains",
            "silence", "tackled", "uniform", "venture", "warrior",
            "yearned", "zealots", "arrange", "balance", "capture",
            "dolphin", "embrace", "fiction", "gravity", "horizon",
            "insider", "justice", "knights", "lasting", "machine",
            "network", "orchids", "plastic", "quality", "remorse",
            "service", "tangent", "updates", "vibrate", "whistle"
        ]
        random_number = rd.randint(0, 99)
        return possible_words[random_number]
    
    def __init__(self, player, level):
        self.word = Round.set_random_word()
        self.board = ['_', '_', '_', '_', '_', '_', '_']
        self.guessed_letters = []
        self.game_over = False
        self.player = player
        self.level = level
        self.tries = 0
    
    def set_tries(self):
        match self.level:
            case "Beginner": self.tries = 7
            case "Easy": self.tries = 6
            case "Medium": self.tries = 5
            case "Hard": self.tries = 4
            case "Expert": self.tries = 3

    def pick_letter(self):
        while True:
            try:
                letter = input("Pick a letter from a-z\n").lower()
                if len(letter) != 1:
                    raise ValueError
                if not letter.isalpha():
                    raise ValueError
                if letter in self.guessed_letters:
                    raise ValueError
                return letter
            except ValueError:
                print("Invalid input. Please pick a single letter from "
                      "a - z, that you have not used earlier.\n")

    def print_round_information(self):
        print("Secret word: ", " ".join(self.board))
        print(f"Remaining tries: {self.tries}")
        print(f"Guessed letters: {self.guessed_letters}\n")

    def check_for_end(self):
        if self.tries == 0:
            print("\nYou've run out of tries! You've lost this round.\n")
            self.game_over = True
            self.player.add_fail()
            input("Press ENTER to continue.")
            return
        if '_' not in self.board: 
            print(f"\nYou guessed the word: {self.word.upper()}." 
                  " You've won this round.\n")
            self.game_over = True
            self.player.add_point()
            input("Press ENTER to continue.")
    
    def update(self, guess):
        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.tries -= 1
            return
        
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.board[index] = letter
        return
    
    def start(self):
        self.set_tries()
        
        while not self.game_over:
            self.print_round_information()
            guess = self.pick_letter()
            self.update(guess)
            self.check_for_end()
        return

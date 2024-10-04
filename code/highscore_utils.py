'''
Highscore utilities for wordguesser.

Functions:
    - get_highscore_path(): Provides path to highscore.json
    - load_highscore(): Loads highscore.json as a dict
    - update_highscore(highscore): writes altered data back to highscore.json
    - compare_scores(existing_score, new_score): Compares player scores and 
      determines if the newer score is a highscore. 
    - sort_scores(scores): Sorts given scores from highest to lowest.
    - print_highscore(highlight=None): Formats and prints highscore file. 
      OPTIONAL: If a certain score should be highlighted, it can be passed. 
    - add_player_score(player_score): If the score is the first or better for
      this player at this level, adds the level to the highscore data.
'''

import json
import os

def get_highscore_path():
    return os.path.join(os.path.dirname(__file__), "..", "data", "highscore.json")


def load_highscore():
    path = get_highscore_path()
    with open(path, "r") as f:
        highscore = json.load(f)
    return highscore


def update_highscore(highscore):
    path = get_highscore_path()
    with open(path, "w") as f:
        json.dump(highscore, f, indent=4)


def compare_scores(existing_score, new_score):
    '''
    Compare two player scores and determine if the newer score is a highscore.

    Comparisons:
    - pf_ratio must be higher than the existing score
    - when pf_ratio is equal, time_spent must be lower than the existing score
    - when time_spent is also equal, the earlier date remains highscore so the 
      function returns False.
    
    Returns boolean value.
    '''
    if new_score['pf_ratio'] == existing_score['pf_ratio']:
        if new_score['time_spent'] == existing_score['time_spent']:
            return False
        return new_score['time_spent'] < existing_score['time_spent']
    return new_score['pf_ratio'] > existing_score['pf_ratio']


def sort_scores(scores):
    '''
    Sorts scores from highest to lowest.
    - First sorts by time_elapsed (second criterium)
    - Then sorts by pf_ratio (first criterium)
    
    Receives a dict
    Returns a dict
    '''
    scores_by_time = sorted(
        scores, 
        key=lambda d: d["time_spent"], 
        reverse=False)
    scores_by_points = sorted(
        scores_by_time, 
        key=lambda d: d["pf_ratio"], 
        reverse=True)
    return scores_by_points


def print_highscore(highlight=None):
    '''
    Formats and prints highscore file.
    For each 'level' it performs the following actions:
    - call sort_scores 
    - format and print header (level)
    - format and print fields (score keys) 
    - format and print rows (score values)
    - When a score is passed to highlight, this player score is amplified.
    '''
    highscore = load_highscore()
    
    for level, player_scores in highscore.items():
        sorted_scores = sort_scores(player_scores)
        
        #  Print header
        print(f"\n\n{level.upper().center(55, '=')}")
        
        #  Print fields
        if len(sorted_scores) == 0: continue
        fields = sorted_scores[0].keys()
        for field in fields:
            print(field.upper().ljust(15), end="")
        print("\n")

        # Print values
        for score in sorted_scores:
            values = score.values()
            for value in values:
                #  Highlight new score
                if score == highlight:
                    highlighted_string = "[" + value + "]"
                    print(highlighted_string.ljust(15), end="")
                    continue
                print(value.ljust(15), end="") 
            print("\n")

    input("\n\nPress ENTER to return to main menu.")

    
def add_player_score(player_score):
    '''
    Formats player score and checks if it needs to be added to highscore data.
    - if a player already has a score at this level, the score is replaced if
      it's higher.
    - if it's the first score for this player at this level, the score is added.
    '''
    highscore = load_highscore()
    level = player_score.pop("level")
    name = player_score["name"]
    is_personal_highscore = True

    for existing_score in highscore[level]:
        if existing_score["name"] == name:
            old_score = existing_score
            is_personal_highscore = compare_scores(existing_score, player_score)
            break

    if is_personal_highscore:
        print("Personal Highscore!")
        highscore[level].append(player_score)
        highscore[level].remove(old_score)
        update_highscore(highscore)
        print_highscore(player_score)
    else:
        print("No personal highscore.")







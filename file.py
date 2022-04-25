import json
from operator import itemgetter

# Save the highscores


def save(highscores):
    with open('scoreboard.json', 'w') as file:
        json.dump(highscores, file)  # save highscores to json file


# Load the highscores


def loadscore():
    try:
        with open('scoreboard.json', 'r') as file:
            highscores = json.load(file)  # Read the json file.
    except FileNotFoundError:
        highscores = []  # Define an empty list if the file doesn't exist.
    # Sorted by the score.
    return sorted(highscores, key=itemgetter(1), reverse=True)

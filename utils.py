import json
from os import getcwd, path
from pathlib import Path

def load_hs():
    """
    Function loads highscore json file.
    If none found it creates one so scores can be saved.
    :return:
    """
    # check if there is already a json file to load
    cwd = path.join(getcwd(), 'highscore.json')
    # if not, create one and return it
    if not path.isfile(cwd):
        Path(cwd).touch()
        return {}
    # if there is, return it
    else:
        with open(cwd) as json_file:
            data = json.load(json_file)
        return data

def save_hs(hs):
    """
    Saves last played highscore to variable
    :return:
    """
    cwd = path.join(getcwd(), 'highscore.json')
    with open(cwd, 'w') as outfile:
        json.dump(hs, outfile)




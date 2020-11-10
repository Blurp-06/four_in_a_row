import json
import json_setup

while(True):
    try:
        with open("SETTINGS.json") as f:
            data = json.load(f)
            break
    except:
        json_setup.setup()

WIDTH = data["WIDTH"]
HEIGHT = data["HEIGHT"]

ROWS = data["ROWS"]
COLLUMNS = data["COLLUMNS"]

DISTANCE_BETEWEEN_ROWS = HEIGHT / ROWS
DISTANCE_BETEWEEN_COLLUMNS = WIDTH / COLLUMNS

RADIUS_PERCENTAGE = data["RADIUS_PERCENTAGE"]

P1 = data["P1"]
P2 = data["P2"]
BACKGROUND = data["BACKGROUND"]
SELECT_COLOR = data["SELECT_COLOR"]
FILLING_COINS = data["FILLING_COINS"]
END_TEXT_COLOR = data["END_TEXT_COLOR"]

SEGMENTS = data["SEGMENTS"]

TITLE = "Four in a row"
import json

# If functions is called makes object and dumps it into a JSON file called "SETTINGS.json".
def setup():
    settings = {
        "WIDTH": 600,
        "HEIGHT": 600,
        "ROWS": 7,
        "COLLUMNS": 7,
        "RADIUS_PERCENTAGE": 0.85,
        "P1": [255, 0, 0],
        "P2": [255, 255, 0],
        "BACKGROUND": [0, 0, 235],
        "SELECT_COLOR": [0, 0, 255],
        "FILLING_COINS": [255, 255, 255],
        "END_TEXT_COLOR": [0, 0, 0, 255],
        "SEGMENTS": 400
    }

    with open("SETTINGS.json", "w") as f:
        json.dump(settings, f, indent=2)
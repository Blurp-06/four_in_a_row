from pyglet import window, app, shapes
from pyglet.text import Label
from pyglet.window import key
from pyglet.graphics import Batch
from settings import *
import win_condition

# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html

window = window.Window(width=WIDTH, height=HEIGHT, caption=TITLE)
background, selected_collumn_batch, coins_batch, white_batch = Batch(
), Batch(), Batch(), Batch()
background_square = shapes.Rectangle(
    0, 0, WIDTH, HEIGHT, color=BACKGROUND, batch=background)
still_going = True

grid_lines = [[], []]

for iteration in range(COLLUMNS):
    grid_lines[0].append(shapes.Line(0 + (DISTANCE_BETEWEEN_COLLUMNS * iteration), 0, 0 + (
        DISTANCE_BETEWEEN_COLLUMNS * iteration), HEIGHT))

for iteration in range(ROWS):
    grid_lines[1].append(shapes.Line(0, 0 + (DISTANCE_BETEWEEN_ROWS * iteration),
                                     WIDTH, 0 + (DISTANCE_BETEWEEN_ROWS * iteration)))
def reset_or_start():
    global position_x, turn, coins
    position_x, turn = 0, P1
    coins = []
    for _ in range(COLLUMNS):
        coins.append([])

reset_or_start()

@window.event
def on_key_press(symbol, modifier):
    global position_x, turn
    # left arrow
    if(symbol == key.LEFT or symbol == key.A):
        if(position_x != 0):
            position_x -= 1
        else:
            position_x = COLLUMNS - 1

    # right arrow
    elif(symbol == key.RIGHT or symbol == key.D):
        if(position_x != COLLUMNS - 1):
            position_x += 1
        else:
            position_x = 0

    elif((symbol == key.SPACE or symbol == key.DOWN or symbol == key.S) and still_going):
        if(len(coins[position_x]) != ROWS):
            coins[position_x].append("r" if turn == P1 else "y")
            if(turn == P1):
                turn = P2
            else:
                turn = P1
    elif(symbol == key.R):
        reset_or_start()


@window.event
def on_draw():
    global still_going

    window.clear()
    window.set_caption(f"{TITLE} - P1" if turn ==
                    P1 else f"{TITLE} - P2")

    white_coins = draw_white_circles()
    select = draw_selection_field()
    c = draw_coins()
    background.draw()
    selected_collumn_batch.draw()
    white_batch.draw()
    coins_batch.draw()

    if(is_a_tie()):
        Label("It's a tie", font_name="Times New Roman", font_size=36, x=WIDTH/2, y=HEIGHT /
            2, anchor_x="center", anchor_y="center", bold=True, color=END_TEXT_COLOR).draw()
        still_going = False

    elif(turn == P2):
        if(win_condition.check_win(coins, "r")):
            Label("P1 wins!", font_name="Times New Roman", font_size=36, x=WIDTH/2, y=HEIGHT /
                2, anchor_x="center", anchor_y="center", bold=True, color=END_TEXT_COLOR).draw()
            still_going = False

    elif(turn == P1):
        if(win_condition.check_win(coins, "y")):
            Label("P2 wins!", font_name="Times New Roman", font_size=36, x=WIDTH/2, y=HEIGHT / 
                2, anchor_x="center", anchor_y="center", bold=True, color=END_TEXT_COLOR).draw()
            still_going = False

def draw_selection_field():
    return shapes.Rectangle(grid_lines[0][position_x].x, 0, DISTANCE_BETEWEEN_COLLUMNS, HEIGHT, color=SELECT_COLOR, batch=selected_collumn_batch)


def draw_coins():
    return_array = []
    i = -1
    for col in coins:
        i += 1
        j = 0
        for coin in col:
            # return_array.append(shapes.Rectangle(grid_lines[0][i].x, j * DISTANCE_BETEWEEN_ROWS, DISTANCE_BETEWEEN_COLLUMNS, DISTANCE_BETEWEEN_ROWS, color=P1 if coin == "r" else P2, batch=coins_batch))
            return_array.append(shapes.Circle(
                grid_lines[0][i].x + DISTANCE_BETEWEEN_COLLUMNS / 2, j * DISTANCE_BETEWEEN_ROWS + DISTANCE_BETEWEEN_ROWS / 2, radius=(DISTANCE_BETEWEEN_ROWS / 2) * RADIUS_PERCENTAGE, segments=SEGMENTS, color=P1 if coin == "r" else P2, batch=coins_batch))
            j += 1

    return return_array


def is_a_tie():
    total_length = 0
    for coin_stack in coins:
        total_length += len(coin_stack)
    return True if total_length == ROWS * COLLUMNS else False


def draw_white_circles():
    return_array = []
    i = -1
    for col in coins:
        i += 1
        j = 0
        for _ in range(COLLUMNS):
            # return_array.append(shapes.Rectangle(grid_lines[0][i].x, j * DISTANCE_BETEWEEN_ROWS, DISTANCE_BETEWEEN_COLLUMNS, DISTANCE_BETEWEEN_ROWS, color=P1 if coin == "r" else P2, batch=coins_batch))
            return_array.append(shapes.Circle(
                grid_lines[0][i].x + DISTANCE_BETEWEEN_COLLUMNS / 2, j * DISTANCE_BETEWEEN_ROWS + DISTANCE_BETEWEEN_ROWS / 2, radius=(DISTANCE_BETEWEEN_ROWS / 2) * RADIUS_PERCENTAGE, segments=SEGMENTS, color=FILLING_COINS, batch=white_batch))
            j += 1

    return return_array


app.run()

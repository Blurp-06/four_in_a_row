from settings import *

# https://stackoverflow.com/questions/29949169/python-connect-4-check-win-function

def check_win(_board: list, tile: str):
    boardHeight = HEIGHT
    boardWidth = WIDTH
    
    board = []
    for col in _board:
        board.append(col.copy())
    for col in board:
        while(len(col) != ROWS):
            col.append("-")

    # check horizontal spaces
    for y in range(boardHeight):
        try:
            for x in range(boardWidth - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True
        except:
            pass

    # check vertical spaces
    for x in range(boardWidth):
        try:
            for y in range(boardHeight - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True
        except:
            pass

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        try:
            for y in range(3, boardHeight):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True
        except:
            pass

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        try:
            for y in range(boardHeight - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        except:
            pass

    return False


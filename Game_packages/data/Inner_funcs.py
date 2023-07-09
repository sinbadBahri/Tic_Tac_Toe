# This module contains most of game's functions and also two important
# variables, "player" and "computer" ; They are wheather 'X' or 'O'.
# Some functions have imported from "module requirement_funcs".

from Game_packages.data.requirements.required_funcs import *
from termcolor import colored

player, computer = x_or_o()


def printGame(board):
    """This simply shows the gameboard along with its following changes"""
    clearBoard()
    j = 1
    for i in board:
        a = "   "
        if j % 3 == 0:
            a = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "blue"), end=a)
        elif i == "O":
            print(colored(f"[{i}]", "magenta"), end=a)
        else:
            print(f"[{i}]", end=a)
        j += 1


def emptySpace(board):
    """Checks if the Gameboard has any empty spaces left or not."""
    return board.count("X")+board.count("O") != 9


def gameStatus(board, winlist, player):
    """Checks the game's status;
    If the player/computer has already won or not."""
    win = True
    for pattern in winlist:
        win = True
        for i in pattern:
            if board[i] != player:
                win = False
                break
        if win:
            break
    return win


def moveFunc(board, winlist, player, move, undo=False):
    """The most important function;
    resieves a move and changes the chosen numbers in gameboard to 'X' or 'O'
    """
    if possibleMove(board, move):
        board[move-1] = player
        win = gameStatus(board, winlist, player)
        if undo:
            board[move-1] = move
        return True, win
    return False, False


def computerMove(board, winlist, player, computer):
    """This function determines computer's move."""
    move = -1
    # First checks if computer can win:
    for i in range(1, 10):
        if moveFunc(board, winlist, computer, i, True)[1]:
            move = i
            break
    # If not,chooses a move to prevent the player from winning:
    if move == -1:
        for j in range(1, 10):
            if moveFunc(board, winlist, player, j, True)[1]:
                move = j
                break
    # Third situation, chooses a random move:
    if move == -1:
        move = randomMove(board)
    return moveFunc(board, winlist, computer, move)


def int_maker():
    while True:
        a = input()
        try:
            a = int(a)
            break
        except IndentationError and ValueError:
            print("Error 43; Try a natural number... ")
    return a

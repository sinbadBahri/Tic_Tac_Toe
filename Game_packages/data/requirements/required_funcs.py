# This module contains all requirements for "module Inner_funcs".

import time
from os import name, system
from random import randint


def clearBoard():
    """This function clears the pervious board to make place forthe new one.
     It also has a seccond countdown :) """
    time.sleep(1)
    if name == "nt":
        system("cls")
    else:
        system("clear")


def randomMove(board):
    """A function which helps computer to choose a random move in game."""
    while True:
        selection = randint(1, len(board))
        if isinstance(board[selection-1], int):
            return selection


def possibleMove(board, move):
    """This function helps the programm to check wheather the chosen  move
    can be used or not ."""
    if move in range(1, 10) and isinstance(board[move-1], int):
        return True
    return False


def x_or_o():
    """A starter for our programm which also gives users the opportunity to
    choose between 'X' and 'O' ."""
    clearBoard()
    print("Welcome to TicTakToe\nChoose wheater you want to be X or O :")
    while True:
        player = input()
        if player.lower() == 'o':
            player = 'O'
            computer = 'X'
            break
        elif player.lower() == 'x':
            player = 'X'
            computer = 'O'
            break
        else:
            print("Error!!\nchoose between 'x' and 'o' please ...")
    print(f"You are : {player}\nComputer is : {computer}")
    return player, computer

from Game_packages.data.Inner_funcs import *

gameboard = list(range(1, 10))
winlist = [(0, 1, 2), (0, 3, 6), (2, 5, 8),
           (8, 7, 6), (2, 4, 6), (0, 4, 8),
           (1, 4, 7), (3, 4, 5)]

printGame(gameboard)
while emptySpace(gameboard):
    print("Your Turn\n(between 1 to 9)")
    move = int_maker()
    moved, won = moveFunc(gameboard, winlist, player, move)
    printGame(gameboard)
    if not moved:
        print("Invalid number! Try again!")
        continue
    if won:
        print(colored("You won!", "green"))
        break
    elif computerMove(gameboard, winlist, player, computer)[1]:
        printGame(gameboard)
        print(colored("You lost!", "red"))
        break
    printGame(gameboard)
print("END GAME")

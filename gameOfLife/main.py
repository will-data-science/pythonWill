'''
Game of Life!
'''

from testGame import TestGame
from board import Board

def main():

    # Create the initial board
    gameBoard = Board(10, 10)

    # Run first iteration
    gameBoard.boardDraw()

    userInput = ''

    while userInput != 'q':
        userInput = input('Pres enter to go to next generation or q to quit')

        if userInput == '':
            gameBoard.boardUpdate()
            gameBoard.boardDraw()

main()

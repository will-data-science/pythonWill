"""
Game of Life!
"""

from board import Board


def main():
    """
    TODO: Update with user inputs for size
    TODO: Update with graphics to show game
    """
    # Create the initial board
    game_board = Board(10, 5)

    # Run first iteration
    game_board.boardDraw()

    user_input = ''

    while user_input != 'q':
        user_input = input('Pres enter to go to next generation or q to quit')

        if user_input == '':
            game_board.boardUpdate()
            game_board.boardDraw()


main()

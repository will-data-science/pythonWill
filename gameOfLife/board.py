from cell import Cell
from random import randint

class Board:

    def __init__(self, rows, columns):
        '''
        Set initial board based on columns & rows
        '''
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for columnCells in range(self.columns)] for rowCells in range(self.rows)]

        self.boardGenerate()

    # Initially generate a game board
    def boardGenerate(self):
        for row in self.grid:
            for column in row:
                # Randomly generate live cells
                maxInt = 2 # Higher number -> less likely to be live
                if (randint(0, maxInt)) == 1:
                    column.statusUpdateLive()

    # Update board with next generation
    def boardUpdate(self):
        print('updating game board')

        # Store cells that will either go to live or to dead
        toLive = []
        toDead = []

        # Cycle through each cell
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):

                currentCell = self.grid[row][column]
                currentStatus = currentCell.isAlive()

                # Get the valid neighbors for each cell
                validNeighbors = self.getValidNeighbors(row, column)
                liveNeighborCount = 0

                for neighbor in validNeighbors:
                    # Check if alive
                    if neighbor.isAlive():
                        liveNeighborCount += 1

                if currentStatus == True:
                    # A live cell will die if there are less than 2 neighbors
                    # A live cell will live if there are exactly 2 or 3 neighbors
                    # A live cell will die if there are more than 3 neighbors
                    if liveNeighborCount < 2 or liveNeighborCount > 3:
                        toDead.append(currentCell)
                    else:
                        toLive.append(currentCell)

                else:
                    # A dead cell will change to live if there are exactly 3 neighbors
                    if liveNeighborCount == 3:
                        toLive.append(currentCell)

        # Update the cells
        for cell in toLive:
            cell.statusUpdateLive()
        for cell in toDead:
            cell.statusUpdateDead()

    # Draw board
    def boardDraw(self):
        '''
        Draws the board in the terminal
        TODO: Update with graphics to replace terminal
        '''
        numRows = 4 # Controls boarder/line break in terminal
        print('\n' * numRows)
        print('printing board')
        for row in self.grid:
            for column in row:
                print(column.getCellStatus(), end = '') # use end to keep on same line
            print() # essentially creates a new line in terminal

    # Given a cell (row/column), find all neighbors
    def findNeighbors(self, row, column):
        '''
        For each cell, get the neighbors
        '''

    def getValidNeighbors(self, cellRow, cellColumn):
        '''
        Check if neighbors are valid (not outside board)
        Returns valid neighbors
        '''

        searchMin = -1 # minimum is 1 row/column before
        searchMax = 2 # maximum is 1 row/column after -> range will go to 2 - 1 = 1

        neighbors = []


        # check cells in rows/columns both before & after
        for row in range(searchMin, searchMax):
            for column in range(searchMin, searchMax):

                rowNeighbor = cellRow + row
                colNeighbor = cellColumn + column

                # By default assume a valid neighbor
                valid = True

                # Not valid if cell and neighbor have same indices
                if rowNeighbor == cellRow and colNeighbor == cellColumn:
                    valid = False

                # Not valid if neighbor is outside number of rows
                elif rowNeighbor < 0 or rowNeighbor >= self.rows:
                    valid = False

                # Not valid if neighbor is outside number of columns
                elif colNeighbor < 0 or colNeighbor >= self.columns:
                    valid = False

                if valid:
                    neighbors.append(self.grid[rowNeighbor][colNeighbor])

        return neighbors

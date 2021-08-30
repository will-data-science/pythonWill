class TestGame:

    def __init__(self):
        self.grid = [
                    ['dead', 'dead', 'dead'],
                    ['dead', 'dead', 'dead'],
                    ['dead', 'dead', 'dead']
                    ]

    def printGame(self):
            for row in self.grid:
                print(row)

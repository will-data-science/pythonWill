class TestGame:

    def __init__(self):
        self.grid = [
                    ['a', 'b', 'c'],
                    ['d', 'e', 'f'],
                    ['g', 'h', 'i']
                    ]

    def printGame(self):
        for row in self.grid:
            print(row)

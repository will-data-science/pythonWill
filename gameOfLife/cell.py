
class Cell:

    def __init__(self):
        '''
        Store initial status of a Cell
        Assume all cells start dead
        '''
        self.status = 'dead'

    # Method to change status of cell to dead
    def statusUpdateDead(self):
        '''
        Update cell statusDead to be dead
        '''
        self.status = 'dead'

    # Method to change status of cell to live
    def statusUpdateLive(self):
        '''
        Update cell status to be live
        '''
        self.status = 'live'

    # method to check if cell is currently alive
    def isAlive(self):
        '''
        Check if cell status is live
        '''
        #print(self.status == 'live')
        if self.status == 'live':
            return True
        return False

    # Method for what board should do

    def getCellStatus(self):
        if self.isAlive():
            return('0')
        return('*')


from api.alphaVantage import getPoints
from plotting.matplotlib import plot

class TestCommand:
    def __init__(self, names, settings):
        self.names = names # list of command names ex: [tp, teleport]
        self.settings = settings
        
    def getNames(self):
        return self.names
        
    async def run(self, message, args):        
        stockName = "TSCO"
        # points = getPoints(7, stockName)
        if len(args) == 0: # ;test
            await plot(message, 'x', 'y', [2, 4, 5, 6], 'plot1.png')
        else: # ;test a
            await plot(message, 'x', 'y', [4, 4, 5, 1], 'plot2.png')
            
            
            
        
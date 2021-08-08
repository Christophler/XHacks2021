
from api.alphaVantage import timeSeriesDailyAdjusted

class TestCommand:
    def __init__(self, names, settings):
        self.names = names # list of command names ex: [tp, teleport]
        self.settings = settings
        
    def getNames(self):
        return self.names
        
    async def run(self, message, args): 
        if len(args) == 1:            
            stockName = args[0]
            json = timeSeriesDailyAdjusted(stockName)
            dayData = json['Time Series (Daily)']
            tempMax = 7
            points = []
            c = 0
            for date in dayData:
                if c > tempMax:
                    break
                c+= 1
                point = dayData[date]['2. high']
                points.append(point)
            print(points)
            
        
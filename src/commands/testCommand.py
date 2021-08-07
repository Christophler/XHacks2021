
from api.alphaVantage import timeSeriesDailyAdjusted, exchangeRates

class TestCommand:
    def __init__(self, names):
        self.names = names # list of command names ex: [tp, teleport]
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        await message.channel.send("pog champ")
        
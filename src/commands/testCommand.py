
from api.alphaVantage import timeSeriesDailyAdjusted, exchangeRates

class TestCommand:
    def __init__(self, names, settings):
        self.names = names # list of command names ex: [tp, teleport]
        self.settings = settings
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        msg = self.settings.getAttribute("ready_message")
        await message.channel.send(msg)
        
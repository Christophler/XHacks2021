
class StocksCommand:
    def __init__(self, names, settings):
        self.names = names
        self.settings = settings
    
    def getNames(self):
        return self.names
    
    async def run (self, message, args):
        stocksList = self.settings.getAttribute("stocks")
        totalMessage = ""
        totalMessage += ("<@" + str(message.author.id) + "> Stock Data Available:\n")
        for stock in stocksList:
            stockName = stock['name']
            totalMessage += ('- ' + stockName + '\n')
        totalMessage += ("Just type `" + self.settings.getAttribute("command_prefix") + "stock <stock_name>` to start")
        await message.channel.send(totalMessage)
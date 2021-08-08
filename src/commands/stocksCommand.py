import discord

class StocksCommand:
    def __init__(self, names, settings):
        self.names = names
        self.settings = settings
    
    def getNames(self):
        return self.names
    
    async def run (self, message, args):
        stocksList = self.settings.getAttribute("stocks")
        totalMessage = ""
        for stock in stocksList:
            stockName = stock['name']
            totalMessage += ('- ' + stockName + '\n')
        totalMessage += ("Just type `" + self.settings.getAttribute("command_prefix") + "stock <stock_name>` to start")

        # build the embed
        embed = discord.Embed(title="EXAMPLE STOCKS", description=totalMessage)
        embed.set_image(url="https://www.marketplace.org/wp-content/uploads/2019/09/stockmarket.jpg?fit=2880%2C1621")
        embed.set_author(name="MoneyMoneyStocksBot", url="https://discord.com/api/oauth2/authorize?client_id=873654361438433300&permissions=8&scope=bot", icon_url="https://www.cnet.com/a/img/uaUy0yK-_-dwdVo_pzqVS3d48hI=/1200x630/2021/04/01/05b0b37a-2c25-4ea0-941c-c9db574e94e5/16br-stonks-motd-1920x1080-1920x1080-d7e1e18d423d.jpg")

        userTag = "<@" + str(message.author.id) + ">\n"
        # send the embed
        await message.channel.send(userTag, embed=embed)
import discord
import os
from plotting.matplotlib import getPlotFile
from api.alphaVantage import getPoints

class PlotCommand:
    def __init__(self, names, settings):
        self.names = names # list of command names ex: [tp, teleport]
        self.xLabel = settings.getAttribute("plot.xLabel")
        self.yLabel = settings.getAttribute("plot.yLabel")
        self.fileName = settings.getAttribute("plot.temp_image_name")
        self.settings = settings
        
    def getNames(self):
        return self.names
        
    # ;plot TSCO
    async def run(self, message, args): 
        if len(args) == 1:
            # get setting things
            desiredStock = None
            for stock in self.settings.getAttribute('stocks'):
                if(stock['name'].lower() == args[0].lower()):
                    desiredStock = stock
                    break
            
            title = desiredStock['name']
            thumbnail_url = desiredStock['image_url']
            
            # get reference to the local plot file 
            pointsY = getPoints(7, title)
            file = await getPlotFile([0, 1, 2, 3, 4, 5, 6], pointsY, self.xLabel, self.yLabel, self.fileName, title)

            # build the embed
            embed = discord.Embed(title=title.upper(), description="Stock Data found on " + title)
            embed.set_image(url=("attachment://"+self.fileName))
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_author(name="MoneyMoneyStocksBot", url="https://discord.com/api/oauth2/authorize?client_id=873654361438433300&permissions=8&scope=bot", icon_url="https://www.cnet.com/a/img/uaUy0yK-_-dwdVo_pzqVS3d48hI=/1200x630/2021/04/01/05b0b37a-2c25-4ea0-941c-c9db574e94e5/16br-stonks-motd-1920x1080-1920x1080-d7e1e18d423d.jpg")
            
            # send the embed
            await message.channel.send(file=file, content=("<@" + str(message.author.id) + ">"), embed=embed)
                    
            # remove the local file
            os.remove(self.fileName)
        else:
            message.channel.send(content=(message.author + "Incorrect usage"))
        
        
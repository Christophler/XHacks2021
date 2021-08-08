import os
import discord
from plotting.matplotlib import plot, getPlotFile

class PlotCommand:
    def __init__(self, names, settings):
        self.names = names # list of command names ex: [tp, teleport]
        self.points = settings.getAttribute("plot.points")
        self.xLabel = settings.getAttribute("plot.xLabel")
        self.yLabel = settings.getAttribute("plot.yLabel")
        self.fileName = settings.getAttribute("plot.temp_image_name")
        
    def getNames(self):
        return self.names
        
    async def run(self, message, args): 

        # get reference to the local plot file 
        file = await getPlotFile(self.points, self.xLabel, self.yLabel, self.fileName)
        
        # build the embed
        embed = discord.Embed(title="TITLE", description="Description")
        embed.set_image(url=("attachment://"+self.fileName))
        embed.set_thumbnail(url="https://g.foolcdn.com/editorial/images/637254/stock-up-glowing-green-arrow-climbs-on-a-stock-screen.jpg")
        embed.set_author(name="XHacks2021", url="https://discord.com/api/oauth2/authorize?client_id=873654361438433300&permissions=8&scope=bot", icon_url="https://g.foolcdn.com/editorial/images/637254/stock-up-glowing-green-arrow-climbs-on-a-stock-screen.jpg")
        
        # send the embed
        await message.channel.send(file=file, content="Content", embed=embed)
        
        # remove the local file
        os.remove(self.fileName)
        
        
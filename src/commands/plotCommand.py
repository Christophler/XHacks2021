import os
import discord
from api.alphaVantage import timeSeriesDailyAdjusted, exchangeRates
from plotting.matplotlib import plot

class PlotCommand:
    def __init__(self, names):
        self.names = names # list of command names ex: [tp, teleport]
        self.xLabel = "test x"
        self.yLabel = "test y"
        self.points = [2, 4, 6, 7, 10]
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        await plot(os,discord,message,self.xLabel,self.yLabel,self.points)
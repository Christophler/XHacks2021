import matplotlib.pyplot as plt
import discord

async def plot(os, message, xLabel, yLabel, points):
  plt.plot(points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = 'plot')
    
  await message.channel.send(file=discord.File('plot.png'))
  os.remove('plot.png')
  
async def getPlotFile(points, xLabel, yLabel, fileName):
  plt.plot(points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = fileName)
  
  file = discord.File(fileName)
  return file
  
  
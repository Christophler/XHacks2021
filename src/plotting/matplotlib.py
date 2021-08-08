import matplotlib.pyplot as plt
import discord
import os

async def plot(message, xLabel, yLabel, points, fname):
  plt.plot(points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = fname)
    
  await message.channel.send(file=discord.File(fname))
  plt.clf()
  os.remove(fname)
  
async def getPlotFile(pointsX, pointsY, xLabel, yLabel, fileName):
  print(pointsX)
  print(pointsY)
  plt.axis([0, 7, 100, 200])
  plt.plot(pointsX, pointsY, 'ro')
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = fileName)
  
  file = discord.File(fileName)
  plt.clf()
  return file
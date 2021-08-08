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
  x = 0
  for i in pointsY:
    pointsY[x] = float(i)
    x = x+1

  print(pointsY)
  plt.plot(pointsX, pointsY)
  plt.axis([1, 5, 180, 194])
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = fileName)
  
  file = discord.File(fileName)
  plt.clf()
  return file
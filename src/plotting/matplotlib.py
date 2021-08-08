import matplotlib.pyplot as plt

async def plot(os,discord,message,xLabel,yLabel,points):
  plt.plot(points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = 'plot')
    
  await message.channel.send(file=discord.File('plot.png'))
  os.remove('plot.png')
  
async def getPlot(discord, points, xLabel, yLabel, fileName):
  plt.plot(points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(fname = fileName)
  
  file = discord.File(fileName)
  return file
  
  
# Importing the needed libraries
import os
import discord
from settings import Settings

# Commands
from commands.plotCommand import PlotCommand
from commands.helpCommand import HelpCommand
from commands.stocksCommand import StocksCommand

# from api.alphaVantage import timeSeriesDailyAdjusted, quotePrice

# Importing the stay awake function
# from stayWake.stay_awake import stay_awake
# Ensures the bot runs 24/7
# stay_awake()

# Setting the discord client variable
bot = discord.Client()

settings = Settings()
commands = [PlotCommand(['plot', 'stock'], settings), HelpCommand(['help'], settings), StocksCommand(['stocks'], settings)]

# Showing that the bot is ready


@bot.event
async def on_ready():
    await bot.get_channel(settings.getAttribute("announce_channel_id")).send(settings.getAttribute("ready_message"))
    print(settings.getAttribute("ready_message"))


# Whenever there's a message, this function runs
@bot.event
async def on_message(message):
    # Ensures that a user is saying the commands and not the bot
    if message.author == bot:
      return
    
    # if the message begins with command prefix
    if len(message.content) > 0 and message.content[0] != settings.getAttribute("command_prefix"):
      return
    
    # Check if the message was a command
    split = message.content.split(' ')
    potentialCmdName = split[0][1::]
    
    done = False
    for cmd in commands:
      cmdNames = cmd.getNames()
      for cmdName in cmdNames:
        if(potentialCmdName == (cmdName)):
          args = []
          if(len(split) > 1):
            for i in range(1, len(split)):
              args.append(split[i])
          await cmd.run(message, args)
          print("Command run: " + potentialCmdName + " " + str(args))
          done = True
          break
      if done:
        break

# Running the bot
# INSERT YOUR BOT TOKEN ID
my_secret = os.environ['discordBot_token']
bot.run(my_secret)

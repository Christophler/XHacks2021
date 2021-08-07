# Importing the needed libraries
import os
import discord

# Commands
from commands.plotCommand import PlotCommand

# Importing the stay awake function
# from stayWake.stay_awake import stay_awake
# Ensures the bot runs 24/7
# stay_awake()

# Setting the discord client variable
bot = discord.Client()

commands = [PlotCommand(['plot'])]

# Showing that the bot is ready


@bot.event
async def on_ready():
    await bot.get_channel(843616163010314260).send("I'm Here")
    print("XHacks2021 is up and ready to roll out")


# Whenever there's a message, this function runs
@bot.event
async def on_message(message):
    # Ensures that a user is saying the commands and not the bot
    if message.author == bot:
      return

    done = False

    for cmd in commands:
      cmdNames = cmd.getNames()
      for cmdName in cmdNames:
        if(message.content.startswith(cmdName)):
          await cmd.run(message)
          done = True
          break
      if done:
        break

# Running the bot
# INSERT YOUR BOT TOKEN ID
my_secret = os.environ['discordBot_token']
bot.run(my_secret)

# Importing the needed libraries
import os
import discord


# Importing the API request function
from api.alphaVantage import timeSeriesDailyAdjusted
from api.alphaVantage import exchangeRates
exchangeRates()

#importing the plotting functions
from plotting.matplotlib import plot
xLabel = "Test x"
yLabel = "Test y"
points = [2, 4, 6, 7, 10]


#Importing the stay awake function
#from stayWake.stay_awake import stay_awake
# Ensures the bot runs 24/7
#stay_awake()

# Setting the discord client variable
bot = discord.Client()


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


  # Help command
  if message.content.startswith(';plot'):
    await plot(os,discord,message,xLabel,yLabel,points)




# Running the bot
# INSERT YOUR BOT TOKEN ID
my_secret = os.environ['discordBot_token']
bot.run(my_secret)
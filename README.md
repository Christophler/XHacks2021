
# About MoneyMoneyStocksBot
MoneyMoneyStocksBot is a discord bot that lets users view recent stock data on a number of select stocks available. It neatly puts the data in a graph to see the stock's progress over the past 7 days. All with one bot and one command, you and your friends can view the stock market with ease.

# Instructions
1. Get the bot on your discord server: https://tinyurl.com/moneymoneystocksbot 
2. Type `;help` to view the commands
3. Type `;stocks` to view the stocks you can preview
4. Type `;stock <name>` to view stock information
5. Enjoy the easy-to-access data!

# Developers
- Install python http request library: `pip install requests`
- Install matplotlib: `pip install matplotlib`
- Set your environment variable for running on local machine. Name the environment variable `discordBot_token`

### Command Template
Every command should have the bare minimum for the main file to process it:
```py
# myCommand.py
class MyCommand:
    def __init__(self, names):
        self.names = names # list of command names ex: [tp, teleport]
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        pass # put code in here
```

### Settings
How to access the settings values (cached in the Settings object). Settings is first initialized in `main.py` and should be passed through functions if needed.
```py
# testCommand.py
class TestCommand:
    def __init__(self, names, settings): # pass in "settings" through the constructor
        self.names = names
        self.settings = settings
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        msg = self.settings.getAttribute("ready_message") # use the "settings" object as needed
        await message.channel.send(msg)

# main.py
from settings import Settings
settings = Settings() # initialize settings
commands = [PlotCommand(['plot']), TestCommand(['test'], settings)] # pass in settings into TestCommand(..,settings)
```

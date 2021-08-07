
# About

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

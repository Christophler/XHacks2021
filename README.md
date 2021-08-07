
# About

# Developers
Get requests (python http handler): 
`pip install requests`

Set your environment variable for running on local machine

## Command Template
Every command should have the bare minimum for the main file to process it:
myCommand.py
```py
class MyCommand:
    def __init__(self, names):
        self.names = names # list of command names ex: [tp, teleport]
        
    def getNames(self):
        return self.names
        
    async def run(self, message): 
        pass # put code in here
```

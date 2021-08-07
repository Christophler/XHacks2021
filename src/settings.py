
import json 

class Settings:
    def __init__(self):
        # initialize cache
        f = open('public/settings.json')
        data = json.load(f)
        self.cache = data
    
    def getAttribute(self, id):
        return self.cache[id]

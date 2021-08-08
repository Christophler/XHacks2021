
import json 

class Settings:
    def __init__(self):
        # initialize cache
        f = open('public/settings.json')
        data = json.load(f)
        self.cache = data
    
    def getAttribute(self, id):
        look = self.cache
        split = id.split('.')
        for nest in split:
            look = look[nest]
        return look

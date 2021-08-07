

class Lobby:
    
    def __init__(self, id):
        self.id = id;
        
    def addUser(self, discordId):
        self.players.append(discordId);

class LobbyHandler:

    def createLobby(self, id):
        lobby = Lobby(id)
        self.lobbies.append(lobby)
        
    def addUser(self, lobbyId, discordId):
        
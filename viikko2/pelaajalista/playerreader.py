import requests
from player import Player

class PlayerReader:
    def __init__(self):
        self.players = []

    def get_players(self, url):
        response = requests.get(url).json()

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)
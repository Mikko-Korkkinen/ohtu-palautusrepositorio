import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader()
    reader.get_players(url)
    all_players = reader.players
    stats = PlayerStats(all_players)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
   
def search_by_nationality(nationality):
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)

        if player.nationality == nationality:
            print(player)

if __name__ == "__main__":
    main()
class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players_from_nationality = []

        for player in self.players:
            if player.nationality == nationality:
                players_from_nationality.append(player)

        return sorted(players_from_nationality, key=lambda player: player.goals + player.assists, reverse=True)
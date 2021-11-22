class Villageois:
    def __init__(self, name):
        self.type = "bot"
        self.name = name

    def set_player(self):
        self.type = "player"

    def turn(self, all_players):
        pass

    def kill(self):
        pass


class LoupGarou(Villageois):
    def turn(self, all_players):
        pass


class Voyante(Villageois):
    def turn(self, all_players):
        if self.type == "player":
            for i, player in enumerate(all_players):
                print(f"{i} - {player.name}")

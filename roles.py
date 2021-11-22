class Villageois:
    def __init__(self):
        self.type = "bot"

    def set_player(self):
        self.type = "player"

    def turn(self, all_players):
        pass

    def kill(self):
        pass


class LoupGarou(Villageois):
    def turn(self, all_players):
        pass

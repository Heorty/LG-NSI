import csv
import random

file = open("./prenom.csv")
csvfile = csv.reader(file)
prenoms = []

for row in csvfile:
    prenoms.append(row[0].split(";")[0].split()[0])


class Villageois:
    def __init__(self):
        self.type = "bot"
        self.name = random.choice(prenoms)

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
            n = int(input("Quelle personne voulez vous sonder ?"))
            name = all_players[n].name
            identity = all_players[n].__class__.__name__
            print(f"Identité de {name} : {identity}")

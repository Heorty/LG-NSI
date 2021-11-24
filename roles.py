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
        self.alive = True

    def set_player(self):
        self.type = "player"

    def turn(self, all_players):
        pass

    def kill(self):
        self.alive = False


class LoupGarou(Villageois):
    def turn(self, all_players, response):
        if self.type == "player":
            print("Choix des autres loups-garous:", " ".join(map(str, response)))
            i = 0
            for player in all_players:
                if player.alive:
                    print(f"{i} - {player.name}")
                    i += 1
            n = int(input("Quelle personne voulez vous tuer ?"))
        else:
            return random.randint(0, sum(player.alive for player in all_players)-1)


class Voyante(Villageois):
    def turn(self, all_players):
        if self.type == "player":
            i = 0
            for player in all_players:
                if player.alive:
                    print(f"{i} - {player.name}")
                    i += 1
            n = int(input("Quelle personne voulez vous sonder ?"))
            name = all_players[n].name
            identity = all_players[n].__class__.__name__
            print(f"Identité de {name} : {identity}")

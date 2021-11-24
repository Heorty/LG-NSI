import csv
import random

file = open("./prenom.csv")
csvfile = csv.reader(file)
prenoms = []

for row in csvfile:
    prenoms.append(row[0].split(";")[0].split()[0])


class Villageois:
    def __init__(self):
        self.classType = "Simple villageois"
        self.type = "bot"
        self.name = random.choice(prenoms)
        self.alive = True

    def set_player(self):
        self.type = "player"

    def turn(self, all_players):
        pass

    def onDeath(self, all_players):
        self.alive = False


class LoupGarou(Villageois):
    def turn(self, all_players, response):
        if self.type == "player":
            print("Choix des autres loups-garous:",
                  " - ".join(map(str, response)))
            i = 0
            for player in all_players:
                if player.alive and not isinstance(player, LoupGarou):
                    print(f"{i} - {player.name}")
                    i += 1
            n = int(input("Quelle personne voulez vous tuer ?"))
        else:
            return random.randint(0, sum(player.alive and not isinstance(player, LoupGarou) for player in all_players)-1)


class Voyante(Villageois):

    def __init__(self):
        super().__init__(2)
        self.classType = "Voyante"

    def turn(self, all_players):
        if self.type == "player":
            i = 0
            for player in all_players:
                if player.alive and not isinstance(player, Voyante):
                    print(f"{i} - {player.name}")
                    i += 1
            n = int(input("Quelle personne voulez vous sonder ?"))
            name = all_players[n].name
            identity = all_players[n].__class__.__name__
            print(f"Identité de {name} : {identity}")

class Chasseur(Villageois):
    def turn(self, all_players):
        pass

    def onDeath(self, all_players):
        if self.type == "player":
            i = 0
            for player in all_players:
                if player.alive:
                    print(f"{i} - {player.name}")
                    i += 1
            n = int(input("Quelle personne voulez vous tuez ?"))
            name = all_players[n].name
            identity = all_players[n].__class__.__name__
            print(f"Identité de {name} : {identity}")


        return super().kill()

class Sorciere(Villageois):
    def turn(self, all_players):
        pass
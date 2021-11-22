import csv
import random

f= open ("./prenom.csv")
csvfile = csv.reader(f)
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

a = Villageois()
print(a.name)
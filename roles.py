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

    def onDeath(self):
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
            return n
        else:
            return random.randint(0, sum(player.alive and not isinstance(player, LoupGarou) for player in all_players)-1)


class Voyante(Villageois):

    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
        self.potions = {
            "save": True,
            "kill": True
        }

    def turn(self, all_players, killed):
        if self.type == "player":
            print(f"Cette personne a été tué: {killed.name}")
            print("Voulez-vous la sauver, ne rien faire ou tuer une autre personne?")
            while True:
                choice = int(input("sauver (0), ne rien faire (1), tuer (2)"))
                if choice == 0:
                    if self.potions["save"]:
                        self.potions["save"] = False
                        return {
                            "saved": True
                        }
                    else:
                        print("vous ne pouvez pas réutiliser cette potion")
                elif choice == 1:
                    return {
                        "saved": False
                    }
                elif choice == 2:
                    if self.potions["kill"]:
                        self.potions["kill"] = False
                        i = 0
                        for player in all_players:
                            if player.alive and not isinstance(player, Sorciere):
                                print(f"{i} - {player.name}")
                                i += 1
                        n = int(input("Quelle personne voulez vous tuez ?"))
                        i = 0
                        for player in all_players:
                            if player.alive and not isinstance(player, Sorciere):
                                if i == n:
                                    killed = player
                                    break
                                i += 1
                        return {
                            "saved": False,
                            "killed": killed
                        }
                    else:
                        print("vous ne pouvez pas réutiliser cette potion")
        else:
            while True:
                choice = random.randint(0, 2)
                if choice == 0 and self.potions["save"]:
                    self.potions["save"] = False
                    return {
                        "saved": True
                    }
                elif choice == 1:
                    return {
                        "saved": False
                    }
                elif choice == 2 and self.potions["kill"]:
                    self.potions["kill"] = False
                    n = random.randint(0, sum(player.alive and not isinstance(player, Sorciere) for player in all_players)-1)
                    i = 0
                    for player in all_players:
                        if player.alive and not isinstance(player, Sorciere):
                            if i == n:
                                killed = player
                                break
                            i += 1
                    return {
                        "saved": False,
                        "killed": killed
                    }




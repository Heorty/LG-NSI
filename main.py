from typing import Dict
import random
import roles


def getName():
    return random.choice(
        ["Laure", "Pablo", "Julien", "Eli", "a", "b", "c", "d", "e", "f"]
    )


players = {
    "villageois": [roles.Villageois(getName()) for _ in range(3)],
    "loups_garous": [roles.LoupGarou(getName()) for _ in range(3)],
    "voyante": [roles.Voyante(getName())]
}
random.choice(list(players.values()))[-1].set_player()


def get_all_players(players: Dict[str, roles.Villageois]):
    p = sum(players.values(), [])
    random.shuffle(p)
    return p


game = True
while game:
    print("Le village s'endort")
    print("La voyante se réveille")
    players["voyante"][0].turn(get_all_players(players))
    print("Les loups-garous se réveillent")
    input("pass")

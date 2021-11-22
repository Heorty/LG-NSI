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
    return sum(players.values(), [])


game = True
while game:
    players["voyante"][0].turn(get_all_players(players))
    input("pass")

from typing import Dict
import random

import lore
import roles



players = {
    "villageois": [roles.Villageois() for _ in range(4)],
    "loups_garous": [roles.LoupGarou() for _ in range(5)],
    "voyante": [roles.Voyante()]
}
random.choice(list(players.values()))[-1].set_player()


def get_all_players(players: Dict[str, roles.Villageois]):
    randomizedPlayers = sum(players.values(), [])
    random.shuffle(randomizedPlayers)
    return randomizedPlayers



game = True


while game:

    players["voyante"][0].turn(get_all_players(players))
    print("Les loups-garous se réveillent")
    response = []
    for loup_garou in players["loups_garous"]:
        response.append(loup_garou.turn(get_all_players(players), response))
    input("pass")

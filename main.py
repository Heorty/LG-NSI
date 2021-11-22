from typing import Dict
import random
import roles


players = {
    "villageois": [roles.Villageois() for _ in range(3)],
    "loups_garous": [roles.LoupGarou() for _ in range(3)]
}
random.choice(list(players.values()))[-1].set_player()


def get_all_players(players: Dict[str, roles.Villageois]):
    return sum(players.values(), [])


game = True
while game:
    for player in get_all_players(players):
        print(player.type)
    input()

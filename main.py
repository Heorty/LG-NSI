from typing import Dict
import random
import roles

def setup():
    pass

def day():
    pass

def night():
    pass

def sideEvent():
    pass

players = {
    "villageois": [roles.Villageois() for _ in range(3)],
    "loups_garous": [roles.LoupGarou() for _ in range(3)]
}
random.choice(list(players.values()))[-1].set_player()


def get_all_players(players: Dict[str, roles.Villageois]):
    return sum(players.values(), [])


game = True


setup()
while game:
    night()
    sideEvent()
    day()

from typing import Dict
import random
import roles
import lore


players = {
    "villageois": [roles.Villageois() for _ in range(4)],
    "voyante": [roles.Voyante()],
    "chasseur": [roles.Chasseur()],
    "sorciere": [roles.Sorciere()],
    "loups_garous": [roles.LoupGarou() for _ in range(7)]
}
random.choice(list(players.values()))[-1].set_player()


def get_all_players(players: Dict[str, roles.Villageois]):
    randomizedPlayers = sum(players.values(), [])
    random.shuffle(randomizedPlayers)
    return randomizedPlayers



game = True


while game:
    lore.finjour()

    lore.voyante(False)
    turn = get_all_players(players)
    players["voyante"][0].turn(turn)
    lore.voyante(True)

    lore.loup_garou(False)
    response = []
    for loup_garou in players["loups_garous"]:
        response.append(loup_garou.turn(turn, response))
    i = 0
    for player in turn:
        if player.alive and not isinstance(player, roles.LoupGarou):
            if i == response[-1]:
                killed = player
                break
            i += 1
    lore.loup_garou(True)

    lore.sorciere(False)
    sorciere_choice = players["sorciere"][0].turn(turn, killed)

    if not sorciere_choice.get("save"):
        killed.onDeath(turn)
    if sorciere_choice.get("killed"):
        sorciere_choice.get("killed").onDeath(turn)
    lore.sorciere(True)


    input("pass")

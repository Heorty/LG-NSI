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

    print("Le village s'endort")
    print("La voyante se réveille")
    turn = get_all_players(players)
    players["voyante"][0].turn(turn)

    print("Les loups-garous se réveillent")
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
    
    print("La sorciere")
    sorciere_choice = players["sorciere"][0].turn(turn, killed)

    input("pass")

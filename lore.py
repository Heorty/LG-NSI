import random

def finjour():
    debphrase = ["il fait froid, les loups-garou rodent dans la nature. le village s'endort malgrès cette insécurité en cette nuit de pleine Lune d'hiver",
                 "apres cette journée epuisante le village se rendort",
                 "les supçons commence à se faire, mais le village, fatigué se rendort..."]
    return random.choice(debphrase)


def voyante(dodo: bool):
    if dodo:
        print("La voyante, épuisée, s'endore")
    else:
        print('la voyante se réveille')


def loup_garou(dodo: bool):
    if dodo:
        print('les loups-garous repus se rendorment et rêvent de prochaine victimes')
    else:
        print('les loups-garou se réveillent')


def sorciere(dodo: bool):
    if dodo:
        print('la sorcière, après avoir épuisé ses potions, se rendort')
    else:
        print("la sorcière se réveille en apprenant la mort d'un villageois")

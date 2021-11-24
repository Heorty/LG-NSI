import random


def finjour():
    jourphrase = ["il fait froid, les loups-garou rodent dans la nature. le village s'endort malgrès cette insécurité en cette nuit de pleine Lune d'hiver",
                  "apres cette journée epuisante le village se rendort",
                  "les supçons commence à se faire, mais le village, fatigué se rendort..."]
    return random.choice(jourphrase)


def voyante(dodo: bool):
    if dodo:
        print("La voyante, épuisée, s'endort")
    else:
        print('la voyante se réveille')


def loup_garoup(dodo: bool):
    if dodo:
        print('ayant choisis leur victimes, les loups-garous repus se rendorment et rêvent de prochaine victimes')
    else:
        print('les loups-garou se réveillent affammés de choisir leur nouvelle victime pour leur repas')


def sorcière(dodo: bool):
    if dodo:
        print('la sorcière, après avoir épuisé ses potions, se rendort')
    else:
        print("la sorcière se réveille en apprenant la mort d'un villageois")


def finnuit():
    phanuit = ["le soleil se lève et le village se réveil",
               "en cette nuit plutôt mouvementé, le village se réveil"]
    return random.choice(phanuit)
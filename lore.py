import random

def finjour():
    debphrase = ["Iil fait froid, les loups-garou rodent dans la nature. Le village s'endort malgrès cette insécurité en cette nuit de pleine Lune d'hiver",
                 "Apres cette journée epuisante le village se rendort",
                 "Les supçons commence à se faire, mais le village, fatigué se rendort..."]
    return random.choice(debphrase)


def voyante(dodo: bool):
    if dodo:
        print("La voyante, épuisée, s'endort")
    else:
        print('La voyante se réveille')


def loup_garou(dodo: bool):
    if dodo:
        print('Ayant choisis leur victimes, les loups-garous repus se rendorment et rêvent de prochaines victimes')
    else:
        print('Les loups-garou se réveillent affammés de choisir leur nouvelle victime pour leur repas')


def sorciere(dodo: bool):
    if dodo:
        print('La sorcière, après avoir épuisé ses potions, se rendort')
    else:
        print("La sorcière se réveille en apprenant la mort d'un villageois")


def finnuit():
    phanuit = ["Le soleil se lève et le village se réveil",
               "En cette nuit plutôt mouvementé, le village se réveil",""]
    return random.choice(phanuit)

def chasseur():
    print("Le chasseur, par son dernier souffle, parti avec la personne qui lui a causé le plus de soupçons")

def vote():
    Pvote = ["il est midi, l'heure de la rénunion des villageois suer la place de la mairie. \nEnsemble ils choisiront pour tenter, par toute leur forces de tuer un  loup et de sauver le plus de villageois",
    "la cloche sonne, c'est l'heure pour les villageois de se retrouver et de décider qui ils vont mettre au buchet... Le choix seras cruciale"]
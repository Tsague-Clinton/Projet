from random import randint

# fonction qui empeche l'utiliateur d'entrer plusieur caratere
def carateres():
    while True:
        try:
            caratere = input("\nEntrer la lettre choisie ")
            assert len(caratere) == 1
            break
        except AssertionError:
            print("\nVous ne devez entrer qu'un seul caractere ")
    return caratere

def int_erreur(texte):
    while True:
        try:
            a = int(input(texte))
            assert a == 1 or a == 2
            break
        except ValueError :
            print("Vous devez entrer soit 1 soit 2  \n")
        except AssertionError:
            print("Vous devez soit 1 soit 2 \n")

    return a

def jeu():
    chaine = "* "
    affiche = []

    indice = randint(0, len(liste_mots)-1)
    reponse = liste_mots[indice]
    taille_reponse = len(reponse)

    vies = taille_reponse + 3
    print(reponse)
    for i in range(0, taille_reponse):
        print("*", end=" ")
        affiche.append("* ")

    while chaine.count("* ") != 0 and vies > 0:
        chaine = ""
        i = 0
        choix = carateres()
        for lettre in reponse:
            if choix == lettre:
                affiche[i] = choix
            i += 1
        chaine = " ".join(affiche)
        print(chaine)
        vies -= 1
        if (vies <= 3 and vies > 0):
            print(f"ATTENTION : Il vous reste {vies} chance")

    return chaine


# liste de reponses possible
liste_mots = ["ali","toto","tamo","leo","jerroy"]
jouer = 1
score = 0

while jouer == 1:
    if jeu().count("* "):
        print("Vous avez gagne")
        score += 2
    else:
        print("Vous avez perdu")

    jouer = int_erreur("Voulez-vous rejouer \n1- OUI \n2- NON ")

print(f"Vous avez changer {score} points")
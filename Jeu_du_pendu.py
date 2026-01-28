from random import randint

def carateres():
    while True:
        try:
            caratere = input("\nEntrer la lettre choisie ")
            assert len(caratere) == 1
            break
        except AssertionError:
            print("\nVous ne devez entrer qu'un seul caractere ")
    return caratere

liste_mots = ["ali","toto","tamo","leo","jerroy"]

score = 0
chaine = "* "
affiche = []

indice = randint(0, len(liste_mots)-1)
reponse = liste_mots[indice]
taille_reponse = len(reponse)

print(reponse)
for i in range(0, taille_reponse):
    print("*", end=" ")
    affiche.append("* ")

while chaine.count("* ") != 0:
    chaine = ""
    i = 0
    choix = carateres()
    for lettre in reponse:
        if choix == lettre:
            affiche[i] = choix
            print("Lettre correct")
        else:
            print("Lettre incorrect")
        i += 1
    chaine = " ".join(affiche)
    print(chaine)



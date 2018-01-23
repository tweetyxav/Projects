# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
contenu = []
i=0

continuer_partie = True # Booléen qui est vrai tant qu'on doit continuer la partie

for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        print(nom_carte)
        print(chemin)
        with open(chemin, "r") as fichier:
            contenuFile = fichier.read()
            contenu.append(contenuFile)
            #print(contenu)
            cartes.append(nom_carte)
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")

for i, nom_carte in enumerate(cartes):
	print(str(i)+" - "+nom_carte)

print("Entrez un numéro de labyrinthe pour commencer à jouer :")
############mettre un controle sur l'entier
idCarte= int(input()) - 1

carte = Carte(cartes[idCarte], contenu[idCarte])
labyrinthe = Labyrinthe(cartes[idCarte], carte.grille, carte.robotPosition)
labyrinthe.afficherGrille()
#labyrinthe.afficherLabyrintheWithPosition("2:2")

print(cartes)
for i, carte in enumerate(cartes):
    print("")
    print("{} - {}".format(i + 1, carte))
    print("{}". format(contenu[0][i]))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...

while continuer_partie:
		action= input().upper()
		if action == "N" or action == "n":
			print("Vous quittez la partie mais elle a ete sauvegardée.")
			continuer_partie = False
		elif type(user_input) == str:
			robotPositionNew = labyrinthe.calculPosition(action)
			if labyrinthe.robotObstacle == "U":
				print("Félicitations ! Vous avez gagné !")
			labyrinthe.afficherGrilleWithPosition(robotPositionNew)
		else:
			print("Labyrinthes existants :")


# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.
Exécutez-le avec Python pour lancer le jeu.
"""
import os
import pickle

from carte import Carte
from labyrinthe import Labyrinthe


# On charge les cartes existantes
cartes = []
contenu = []
i=0
continuer_partie = True # Booléen qui est vrai tant qu'on doit continuer la partie

def consigne():
	print("\nactions possible:")
	print("- Q qui doit permettre de sauvegarder et quitter la partie en cours ;\n\
- H aide ;\n\
- N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) ;\n\
- E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) ;\n\
- S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) ;\n\
- O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) ;\n\
- Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).\n\
- Le numéro d'une nouvelle grille pour commencer une nouvelle partie\n")
	

consigne()
if os.path.isfile("saveParty.svg") and os.path.getsize("saveParty.svg") > 0:
		print("Il y a une partie sauvegardée")

carte = Carte() #Initialise les cartes qui se trouvent dans le repertoire carte
# On affiche les cartes existantes
print("Labyrinthes existants :") 
for i, nom_carte in enumerate(carte.cartes):
	print(str(i)+" - "+nom_carte["nomCarte"])

print("Entrez un numéro de labyrinthe ou restaurer une sauvegarde avec R pour commencer à jouer :")

while continuer_partie:
		action= input().upper()
		
		if action == "Q": #quitte le jeu
			print("Vous quittez la partie mais elle a été sauvegardée.")
			continuer_partie = False

		elif action == "R": #recharge la sauvegarde
			if os.path.getsize("saveParty.svg") > 0:
				with open("saveParty.svg", 'rb') as fichier:
					mon_depickler = pickle.Unpickler(fichier)
					labyrinthe = mon_depickler.load()
			print("La sauvegarde a été restaurèe.\n")
			labyrinthe.afficherGrille()

		elif action == "H": #affiche les consigne
			consigne()
			print()

		elif type(action[0:0]) == str and action[1:].isdigit(): #Effectu un mouvement du robot
			robotPositionNew = labyrinthe.calculPosition(action)
			labyrinthe.afficherGrilleWithPosition(robotPositionNew)
			if labyrinthe.robotObstacle == "U":
				print("Félicitations ! Vous avez gagné !")
				consigne()	

		elif action.isdigit() and int(action) < len(carte.cartes): #charge un labyrinthe
			print("Charge le labyrinthe "+action+" "+carte.cartes[int(action)]["nomCarte"])
			idCarte = int(action)
			carte = carte.creerGrilleDepuisChaine(idCarte)
			labyrinthe = Labyrinthe(idCarte, carte.grille, carte.robotPosition)
			labyrinthe.afficherGrille()	

		else:
			consigne()
			#elif type(user_input) == int:


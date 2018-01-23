# -*-coding:Utf-8 -*

import os
import pickle

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:
	"""Classe représentant un labyrinthe."""


	def saveParty(self):
		with open(self.saveFile, 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self)

	def restoreParty(self):
		if os.path.getsize(self.saveFile) > 0:
			with open(self.saveFile, 'rb') as fichier:
				mon_depickler = pickle.Unpickler(fichier)
				self = mon_depickler.load()
				print(self)
		else:
			print("Il n'y a pas de sauvegarde.")

	
	def afficherGrille(self):
		"""Affiche le labyrinthe."""
		ligneStr=""
		for i, ligne in enumerate(self.grille):
			for j, case in enumerate(ligne):
				if case == "/n":
					ligne =  "" #supprime le caractere de retour a la ligne
				else:
					ligneStr = ligneStr + str(case)
			print(ligneStr) #affiche une ligne de la grille
			ligneStr="" #reinitialise la ligne pour uafficher la suivante
		print()


	def afficherGrilleWithPosition(self, robotPosition):
		"""Affiche le grille avec la nouvelle position."""
		grille = self.grille
		grille[self.robotPosition["y"]][self.robotPosition["x"]] = self.robotObstacle #remet l'ancien obstacle a la place du robot
		self.robotObstacle = grille[robotPosition["y"]][robotPosition["x"]] #sauvegarde le type de case cible exemple une porte
		grille[robotPosition["y"]][robotPosition["x"]] = "X" #Met la nouvelle position a jour
		#Memorise la position pour le prochain coup
		self.robotPosition["y"] = robotPosition["y"]
		self.robotPosition["x"] = robotPosition["x"]
		#affiche le grille
		self.afficherGrille() #affiche la grille
		self.saveParty() #sauvegarde la partie
		

	def __init__(self, idCarte="", grille="", robotPosition={"x":0,"y":0}, robotObstacle=" "):
		self.saveFile = "saveParty.svg"
		if idCarte=="":
			self = self.restoreParty()
		else:
			self.idCarte = idCarte
			#robotPosition = robotPosition.split(":")
			self.robotPosition = {"x":robotPosition["x"], "y":robotPosition["y"]}
			self.robotObstacle = robotObstacle
			self.grille = grille


	def __str__(self):
	    sb = []
	    for key in self.__dict__:
	        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
	    return ', '.join(sb)

	 
	def __repr__(self):
	    return self.__str__() 


	def calculPosition(self, robotMouvement):
		"""Calcul la position du robot suite a un mouvement."""
		mouvementY = robotMouvement[0]
		mouvementX = int(robotMouvement[1:])
		robotPositionCible=self.robotPosition

		#defini le sens de deplacement
		if(mouvementY=="N"):
			mouvementY = "S"
			mouvementX = -mouvementX
		if(mouvementY=="O"):
			mouvementY = "E"
			mouvementX = -mouvementX
		#defini le sens de deplacement, permet de gerer des s-2
		if 1 <= mouvementX:
			step=1
		else:
			step=-1

		if(mouvementY=="S"):
			for x in range(step, mouvementX + step, step):	
				if len(self.grille) <= self.robotPosition["y"] + x or len(self.grille[0]) <= self.robotPosition["x"]:
					print("sort de la grille")
					break #rencontre un mur et donc s'arrete
				elif self.grille[self.robotPosition["y"] + x][self.robotPosition["x"] ] == "O":
					print("bloqué par un mur")
					break #rencontre un mur et donc s'arrete
				else:
					robotPositionCible = {"x":self.robotPosition["x"], "y":self.robotPosition["y"] + x}
		if(mouvementY=="E"):
			for x in range(step, mouvementX + step, step):
				if len(self.grille) <= self.robotPosition["y"] or len(self.grille[0]) <= self.robotPosition["x"] + x:
					print("sort de la grille")
					break #rencontre un mur et donc s'arrete
				elif self.grille[self.robotPosition["y"]][self.robotPosition["x"] + x] == "O":
					print("bloqué par un mur")
					break #rencontre un mur et donc s'arrete
				else:
					robotPositionCible = {"x":self.robotPosition["x"] + x, "y":self.robotPosition["y"]}
		return robotPositionCible #retourne la position cible calculee



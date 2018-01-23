# -*-coding:Utf-8 -*

import os

"""Ce module contient la classe Carte."""

class Carte:

	"""Objet de transition entre un fichier et un grille."""

	def __init__(self):
		self.id = "" #ID de la grille selectionnee
		self.robotPosition = {"x":0, "y":0} #position du robot sur la grille selectionnee
		self.grille = "" #grille selectionnee
		self.cartes = [] #contient toutes les grilles au format [{"nomCarte", "contenuFile"}]
		self.lireLaListeDesCartesDisponible() #charge toutes les cartes disponible

	def __repr__(self):
		return "<Carte {}>".format(self.cartes)

	def lireLaListeDesCartesDisponible(self):
		"""Lecture de toutes les grilles se trouvant dan le repertoire cartes au format xxx.txt"""
		for nom_fichier in os.listdir("cartes"):
		    if nom_fichier.endswith(".txt"):
		        chemin = os.path.join("cartes", nom_fichier)
		        nomCarte = nom_fichier[:-3].lower()
		        with open(chemin, "r") as fichier:
		            contenuFile = fichier.read()
		            self.cartes.append({"nomCarte":nomCarte, "contenuFile":contenuFile})

	
	def creerGrilleDepuisChaine(self, idCarte):
		"""Cette fonction creer. le grille a partir de la String dans une list de list."""
		self.id = idCarte
		grille = []
		line=[]
		lineNum=0
		j=0
		for i, case in enumerate(self.cartes[idCarte]["contenuFile"]):
			if case == '\n': #changement de ligne de la grille
				grille.append(line)
				j=j+1
				lineNum=0
				line=[]
				#grille = grille[j].append("O")
			elif case == 'X': #memorise la position du robot sur la grille
				self.robotPosition["x"] = lineNum
				self.robotPosition["y"] = j
				#robotPositionY = j
				#print(robotPositionY)
				line.append(case)
				lineNum=lineNum+1
			else: #memorise toute les case de la grille dans une liste
				line.append(case)
				lineNum=lineNum+1
		self.grille = grille
		return self

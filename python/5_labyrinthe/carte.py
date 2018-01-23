# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

	"""Objet de transition entre un fichier et un grille."""

	def __init__(self, nom, chaine):
		self.nom = nom
		self.robotPosition = {"x":0, "y":0}
		self.grille = self.creerLabyrintheDepuisChaine(chaine)

	def __repr__(self):
		return "<Carte {}>".format(self.nom)



	"""Cette fonction creer. le grille a partir de la String dans une list de list."""
	#############################memoriser ou se trouve la position du X
	def creerLabyrintheDepuisChaine(self, chaine):
		grille = []
		line=[]
		lineNum=0
		j=0
		for i, case in enumerate(chaine):
			if case == '\n':
				grille.append(line)
				j=j+1
				lineNum=0
				line=[]
				#grille = grille[j].append("O")
			elif case == 'X':
				print(self.robotPosition)
				self.robotPosition["x"] = lineNum
				self.robotPosition["y"] = j
				print("self.RobotPosition")
				print(self.robotPosition)
				#robotPositionY = j
				#print(robotPositionY)
				line.append(case)
				lineNum=lineNum+1
			else:
				line.append(case)
				lineNum=lineNum+1
		print(grille)
		return grille
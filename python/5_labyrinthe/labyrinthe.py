# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	"""Affiche le labyrinthe."""
	def afficherGrille(self):
		ligneStr=""
		for i, ligne in enumerate(self.grille):
			for j, case in enumerate(ligne):
				#print("case"+case)
				if case == "/n":
					#print(ligne)
					ligne =  ""
				else:
					#print(ligne)
					ligneStr = ligneStr + str(case)
					#ligne = ligne + case
			print(ligneStr)
			ligneStr=""
		#print(grille)


	"""Affiche le grille avec la nouvelle position."""
	def afficherGrilleWithPosition(self, robotPosition):
		grille = self.grille
		#remet le type de case quittee exemple une porte
		#labyrinthe[self.RobotPositionX][self.positionY] = self.robotObstacle
		#remet l'ancien obstacle a la place du robot
		grille[self.robotPosition["y"]][self.robotPosition["x"]] = self.robotObstacle
		#sauvegarde le type de case cible exemple une porte
		self.robotObstacle = grille[robotPosition["y"]][robotPosition["x"]]
		#Met la nouvelle position a jour
		grille[robotPosition["y"]][robotPosition["x"]] = "X"
		self.robotPosition["y"] = robotPosition["y"]
		self.robotPosition["x"] = robotPosition["x"]
		#affiche le grille
		self.afficherGrille()

	def __init__(self, nomCarte, grille, robotPosition={"x":0,"y":0}, robotObstacle=" "):
		self.nomCarte = nomCarte
		#robotPosition = robotPosition.split(":")
		self.robotPosition = {"x":robotPosition["x"], "y":robotPosition["y"]}
		self.robotObstacle = robotObstacle
		self.grille = grille


	def calculPosition(self, robotMouvement):
		mouvementY = robotMouvement[0]
		mouvementX = int(robotMouvement[1:])
		robotPositionCible=self.robotPosition
		#print("robotPositionCible1")
		#print(robotPositionCible)

		#defini le sens de deplacement
		if(mouvementY=="N"):
			#print("bouge vers le N")
			mouvementY = "S"
			mouvementX = -mouvementX
		if(mouvementY=="O"):
			#print("bouge vers le O")
			mouvementY = "E"
			mouvementX = -mouvementX
		if 1 <= mouvementX:
			step=1
		else:
			step=-1

		if(mouvementY=="S"):
			#print("bouge vers le S")
			#print("mouvement"+str(mouvementX)+"step"+str(step))
			for x in range(step, mouvementX + step, step):
				#print ( "y"+str(self.robotPosition["y"] + x) + "x"+str(self.robotPosition["x"]))
				#print("taille"+ str(len(self.grille))+" "+str(len(self.grille[0])))	
				if len(self.grille) <= self.robotPosition["y"] + x or len(self.grille[0]) <= self.robotPosition["x"]:
					print("sort de la grille")
					break #rencontre un mur et donc s'arrete
				elif self.grille[self.robotPosition["y"] + x][self.robotPosition["x"] ] == "O":
					print("bloqué par un mur")
					break #rencontre un mur et donc s'arrete
				else:
					robotPositionCible = {"x":self.robotPosition["x"], "y":self.robotPosition["y"] + x}
					#print("robotPositionCible1")
					#print (robotPositionCible)
		if(mouvementY=="E"):
			#print("bouge vers le E")
			for x in range(step, mouvementX + step, step):
				#print ( "y"+str(self.robotPosition["y"]) + "x"+str(self.robotPosition["x"] + x) + self.grille[self.robotPosition["y"]][self.robotPosition["x"] + x] )
				if len(self.grille) <= self.robotPosition["y"] or len(self.grille[0]) <= self.robotPosition["x"] + x:
					print("sort de la grille")
					break #rencontre un mur et donc s'arrete
				elif self.grille[self.robotPosition["y"]][self.robotPosition["x"] + x] == "O":
					print("bloqué par un mur")
					break #rencontre un mur et donc s'arrete
				else:
					robotPositionCible = {"x":self.robotPosition["x"] + x, "y":self.robotPosition["y"]}
					#print("robotPositionCible1")
					#print (robotPositionCible)

		#print("robotPositionCible2")
		#print (robotPositionCible)
		return robotPositionCible


import fonctions
import donnees
from random import randrange

mots = donnees.mots
nombre_chance = donnees.nombre_chance

lettre=""

while lettre != "0":
	num_mot_selectionne = randrange(len(mots))
	print(num_mot_selectionne)
	mot_selectionne = mots[num_mot_selectionne]
	mot_trouve = "********"
	print(mot_selectionne)

	print("le mot a ete selectionne, le jeux commence, vous avez "+str(nombre_chance)+"pour trouver le mot")
	i=0
	while lettre != "0" and i<nombre_chance:

	    print("Tapez '0' pour quitter., ou une lettre.")
	    lettre = input()
	    if lettre==0:	#quitte
	    	break
	    if len(lettre)>1 and en(lettre)==0:
	    	print("Vous avez saisie plus d'une lettre.")
	    	continue

	    index = mot_selectionne.find(lettre)
	    print(index)
	    if index == -1:
	    	print('Cette lette n''est pas dans le mot')
	    else:
	        mot_trouve = fonctions.afficher_mot(mot_selectionne, mot_trouve, lettre)
	    i+=i
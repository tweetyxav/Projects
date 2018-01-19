# -*- coding: utf8 -*-
#structures conditionnelles if

annee = input("Saisissez une année : ")

try: # On essaye de convertir l'année en entier
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

print( annee%4)
if annee%4 != 0:
	annee_bissextile=False
else:
	if annee%100 == 0:
		if annee%400 == 0:
			annee_bissextile=True
		else:
			annee_bissextile=False
	else:
		annee_bissextile=True

if annee_bissextile:
	print( "Anne bissextile")
else:
	print( "Anne NON bissextile")


if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
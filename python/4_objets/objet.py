

chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""

while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()


############  LISTE list      #########################
#operation sur une liste
liste_origine = [0, 1, 2, 3, 4, 5]
print( [nb * nb for nb in liste_origine] )

#operation sur une liste avec filtre
qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
[nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer]   #[8, 11, 14]

inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
	]
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
# On reconstitue l'inventaire trié
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, reverse=True)]
print(inventaire)
############  END LISTE       #########################

############  DICTIONNAIRE dict       #########################
fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))
############  END DICTIONNAIRE dict       #########################


############  Fichier       #########################
import os
os.chdir("/Users/eloxav/Serveur/Python")

mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write("Premier test d'écriture dans un fichier via Python")
mon_fichier.close()

with open('fichier.txt', 'r') as mon_fichier:
    texte = mon_fichier.read()


score = {
   "joueur 1":    5,
   "joueur 2":   35,
   "joueur 3":   20,
   "joueur 4":    2,
 }
with open('donnees', 'wb') as fichier:
     mon_pickler = pickle.Pickler(fichier)
     mon_pickler.dump(score)
 

with open('donnees', 'rb') as fichier:
     mon_depickler = pickle.Unpickler(fichier)
     score_recupere = mon_depickler.load()
############  END Fichier       #########################


def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:2]])

print(afficher_flottant(3.99999999999998))









prenom = "Paul"
nom = "Dupont"
age = 21

print( "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} ans.".format(prenom, nom, age, nom.upper()))
# formatage d'une adresse
adresse = """ {no_rue}, {nom_rue} {code_postal} {nom_ville} ({pays})""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

print("Merci !")
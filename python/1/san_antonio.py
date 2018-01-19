# -*- coding: utf8 -*-
import random
import json
print ("yoyo") 

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

def read_values_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values 
    # Create a new empty list
    # open a json file with my objects
    # load all the data contained in this file
    # add each item in my list
    # return my completed list

print("read_values_from_json : " + read_values_from_json("quotes.json", 1))


characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item_in(my_list):
	rand_numb = random.randint(0, len(my_list) - 1) # get a random number
	item = my_list[rand_numb] # get a quote from a list
	print(item) # show the quote in the interpreter
	return "program is over" # returned value


def create_message(character, quote):
    return "{} a dit : {}".format(character, quote)

user_answer = raw_input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


while user_answer != "B":
	print(get_random_item_in(quotes))
	user_answer = raw_input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')
	print(user_answer)

print(create_message("character", "quote"))


#manipuler list

characters = ["tic", "tac", "Picsou", "mickey", "mini"]

characters.remove("Picsou")
characters.insert(5,"Mowgli")
characters[4]="Balou"
print(characters)






if user_answer == "B":
		pass
elif user_answer == "C":
	print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
	pass



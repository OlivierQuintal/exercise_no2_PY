#10.	Faites un programme qui compte le nombre de mots dans une ligne de texte.

phrase = input("Entrez une phrase: ")
splitPhrase = phrase.split(" ")
print("Il y a " + str(len(splitPhrase)) + " mots dans cette phrase.")
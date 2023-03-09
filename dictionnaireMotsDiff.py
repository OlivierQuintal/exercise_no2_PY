#14.	Faites un programme qui associe dans un dictionnaire les mots différents d’un texte (la clé) à leur nombre d’occurrences dans le texte (la valeur).

f = open("fichier.txt")
lignes = f.read()
f.close()

listeMots = lignes.split(" ")

dictionnaireMotsDiff = {}

for i in listeMots:
    if i.lower() not in dictionnaireMotsDiff:
        dictionnaireMotsDiff[i.lower()] = 1
    else:
        dictionnaireMotsDiff[i.lower()] += 1
print (dictionnaireMotsDiff)

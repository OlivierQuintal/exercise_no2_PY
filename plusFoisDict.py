# 15.	À partir du dictionnaire de l'exercice 14, affichez la liste des mots qui se retrouvent plus d'une fois dans le texte

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


for motPlusUneFois in dictionnaireMotsDiff:
    if dictionnaireMotsDiff[motPlusUneFois] > 1:
        print(motPlusUneFois)
print (dictionnaireMotsDiff)
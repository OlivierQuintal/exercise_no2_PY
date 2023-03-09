# 13.	Faites un programme qui affiche la liste de tous les mots différents (sans tenir compte de la casse) d’un fichier texte de plusieurs lignes 

f = open("fichier.txt")
lignes = f.read()
f.close()

listeMots = lignes.split(" ")

listeMotsDifferent = []

for i in listeMots:
    if i.lower() not in listeMotsDifferent:
        listeMotsDifferent.append(i.lower())
print (listeMotsDifferent)
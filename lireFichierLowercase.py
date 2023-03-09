#5.	Faites un programme qui met dans une liste en minuscules tous les mots d’un fichier dans lequel 
#il n’y a qu’une seule ligne de texte (par exemple créer la liste ['bonjour', 'tout', 'le', 'monde'] à partir d’un fichier qui contient « Bonjour tout le monde »)

f = open("fichier.txt")
lignes = f.readlines()
f.close()

print(lignes[0].lower())

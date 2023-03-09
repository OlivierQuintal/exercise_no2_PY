#11.	Faites un programme qui compte le nombre de mots dans un fichier qui contient une seule ligne de texte.

f = open("fichier.txt")
lignes = f.readlines()
f.close()

listeMots = lignes[0].split(" ")
print("Il y a ", str(len(listeMots)) , " mots dans ce fichier.")
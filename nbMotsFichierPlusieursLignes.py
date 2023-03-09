#11.	Faites un programme qui compte le nombre de mots dans un fichier qui contient une seule ligne de texte.

f = open("fichier.txt")
lignes = f.read()
f.close()

nbmots = len(lignes.split(" "))
print("Il y a ", (nbmots) , " mots dans ce fichier.")
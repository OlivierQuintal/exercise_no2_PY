#1.	Faire un programme qui extrait le nom de fichier d’un chemin complet.
chemin = "C:/Users/oliqu/OneDrive/Bureau/fichier.txt"

splitChemin = chemin.split('/')
print(splitChemin[-1])


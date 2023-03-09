# 2.	Prendre un nom écrit normalement (Olivier Tardif) et le convertir en format pseudo-administratif (TARDIF, Olivier).

nom = input("Entrez votre nom: ")

splitNom = nom.split(' ')
prenom = splitNom[0]
nomFamille = splitNom[1]

print (nomFamille.upper() + ", " + prenom[0].upper() + prenom[1:].lower())
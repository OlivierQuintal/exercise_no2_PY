#3.	Créer un login à partir d’un nom (initiale du prénom, 6 lettres du nom de famille max)

nom = input("Entrez votre nom: ")

splitNom = nom.split(' ')
prenom = splitNom[0]
nomFamille = splitNom[1]
login = prenom[0].lower() + nomFamille[0:6].lower()
print(login)

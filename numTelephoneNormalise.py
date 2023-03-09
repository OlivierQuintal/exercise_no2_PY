#4.	Faites un programme qui normalise le format d’un numéro de téléphone entré par 
#l’utilisateur et l’affiche ensuite : par exemple 514.343.1436, 514-343-1436 ou (514) 343.1436 doivent être affichés comme (514) 343-1436.

numTelephone = input("Entrez votre numéro de téléphone: ")
numTelephone = numTelephone.replace(" ", "-")
numTelephone = numTelephone.replace(".", "-")

splitNumTelephone = numTelephone.split("-")


numTelephone = numTelephone.replace("(", "")
numTelephone = numTelephone.replace(")", "")

print("(" + splitNumTelephone[0] + ") " + splitNumTelephone[1] + "-" + splitNumTelephone[2])


# RETOURNE (514) 343-1436
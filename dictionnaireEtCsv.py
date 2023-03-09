#7.	Faites un programme qui crée un dictionnaire pour chaque ligne du fichier CSV suivant et le met dans une liste :

f= open("fichiercsv.txt")
lignes = f.readlines()
f.close()
d = {}
listeDictionnaire = []
cle = ['nom', 'prenom', 'datenaiss', 'id']
for ligne in lignes:
    liste = ligne.split(';')
    print(liste[0])
    d[cle[0]] = liste[0]
    d[cle[1]] = liste[1]
    d[cle[2]] = liste[2]
    d[cle[3]] = liste[3]
    listeDictionnaire.append(d)
print(listeDictionnaire)


#ne fonctionne pas trop 
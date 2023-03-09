#6.	Faites un programme qui crée un dictionnaire ayant les clés « nom », « prénom », « datenaiss » et « id » à partir de la 
#chaîne de caractères « Einstein;Albert;1879-03-14;299792458 »

info = "Einstein;Albert;1879-03-14;299792458"
liste = info.split(';')
d = {}
d['nom'] = liste[0]
d['prenom'] = liste[1]
d['datenaiss'] = liste[2]
d['id'] = liste[3]
print("le dictionnaire est: ", d)

#{'nom': 'Einstein', 'prenom': 'Albert', 'datenaiss': '1879-03-14', 'id': '299792458'}
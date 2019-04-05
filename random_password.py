"""
@name random_password
@author Aélion
@version 1.0.0
"""
import random
import string
"""
Tirage longueur mot de passe
et nombre de caractères de chaque type
"""
lengthPassword = random.randint(8,12)
print(lengthPassword)
nbMaj = random.randint(1,lengthPassword-2)
print(nbMaj)
nbPonct = random.randint(1,lengthPassword-1-nbMaj)
print(nbPonct)
nbNum = random.randint(1,lengthPassword-nbMaj-nbPonct)
print(nbNum)
if lengthPassword-nbMaj-nbPonct-nbNum > 0:
    nbMin = lengthPassword-nbMaj-nbPonct-nbNum
else:
    nbMin = 0
print(nbMin)
"""
Listes de caractères utilisés
"""
listPonct = ["*", ",", ";", "/", "+", "-", "(", ")", "[", "]" ]
"""
Déclaration tableaux contenant les caractères du mot de passe
"""
passMaj = []
passPonct = []
passNum = []
passMin = []
"""
Remplissage tableaux
"""
for i in range(nbMaj):
    passMaj.append((random.choice(string.ascii_letters)).upper())
print(passMaj)
for i in range(nbPonct):
    passPonct.append(random.choice(listPonct))
print(passPonct)
for i in range(nbNum):
    passNum.append(str(random.randint(0,9)))
print(passNum)
for i in range(nbMin):
    passMin.append((random.choice(string.ascii_letters)).lower())
print(passMin)

"""
Génération du mot de passe final
"""
passComplete = passMaj+passPonct+passNum+passMin
print(passComplete)
random.shuffle(passComplete)
print(passComplete)

passString = ""
for i in range(len(passComplete)):
    passString = passString + str(passComplete[i])
#OU BIEN
#print("".join(passComplete))

print("Your password:\n",passString)
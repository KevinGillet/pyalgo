"""
@name rendu_monnaie.py
@version 0.0.1
Calcul de rendu de monnaie 
à partir d'un montant lu
"""
#Lecture du montant
montant = 77.53
print("Vous devez", montant, "€")
somme = 100
print("Montant donné :", somme, "€")
#Calcul de la monnaie
monnaie = somme - montant
billet100 = monnaie // 100
rendu100 = monnaie % 100
billet50 = rendu100 // 50
rendu50 = rendu100 % 50
billet20= rendu50 // 20
rendu20 = rendu50 % 20
billet10 = rendu20 // 10
rendu10 = rendu20 % 10
billet5 = rendu10 // 5
rendu5 = rendu10 % 5
piece2 = rendu5 // 2
rendu2 = rendu5 % 2
piece1 = rendu2 // 1
rendu1 = rendu2 % 1
piece50c = (rendu1*100) // 50
rendu50c = (rendu1*100) % 50
piece20c = (rendu50c) // 20
rendu20c = (rendu50c) % 20
piece10c = (rendu20c) // 10
rendu10c = (rendu20c) % 10
piece5c = (rendu10c*100) // 5
rendu5c = (rendu10c*100) % 5
piece2c = (rendu5c*100) // 2
rendu2c = (rendu5c*100) % 2
piece1c = (rendu2c*100) // 1
rendu1c = (rendu2c*100) % 1
#Affichage du rendu
print("Rendu :", monnaie, "€")
if billet100 != 0:
    print(billet100, "x 100€")
if billet50 != 0:
    print(billet50, "x 50€")
if billet20 != 0:
    print(billet20, "x 20€") 
if billet10 != 0:
    print(billet10, "x 10€") 
if billet5 != 0:
    print(billet5,"x 5€") 
if piece2 != 0:
    print(piece2, "x 2€") 
if piece1 != 0:
    print(piece1, "x 1€") 
if piece50c != 0:
    print(piece50c, "x 50c") 
if piece20c != 0:
    print(piece20c, "x 20c") 
if piece10c != 0:
    print(piece10c, "x 10c") 
if piece5c != 0:
    print(piece5c, "x 5c") 
if piece2c != 0:
    print(piece2c, "x 2c") 
if piece1c != 0:
    print(piece1c, "x 1c") 
#print(billet50, billet20, billet10, billet5, piece2, piece1)
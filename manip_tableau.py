"""
@name manip_tableau.py
@author Aélion
@version 1.0.0
Algorithmique spécifique sur les collections
"""

#Déclaration du tableau
monTablo = [15, 3, 25, 12, 7, -15]

#Loop
print("All values times 2:")
#Solution 1
#for indice, val in enumerate(monTablo):
#    print(monTablo[indice] * 2)
#Solution 2
for indice in range(len(monTablo)):
    print(monTablo[indice] * 2)

#More complex loop with condition
print("All values with even indexes times 2:")
for indice in range(len(monTablo)):
    if indice % 2 == 0:
        print(monTablo[indice] * 2)

#Print minimum value of array
print("Minimum value from array:")
minValue = monTablo[0]
for indice in range(1,len(monTablo)):
    if monTablo[indice] < minValue:
        minValue = monTablo[indice]
print(minValue)

#Print maximum value of array
print("Maximum value from array:")
maxValue = monTablo[0]
for indice in range(1,len(monTablo)):
    if monTablo[indice] > maxValue:
        maxValue = monTablo[indice]
print(maxValue)

#Print sum of array values
print("Sum of array values:")
sumArray = 0
for indice in range(len(monTablo)):
    sumArray = sumArray + monTablo[indice]
print(sumArray)
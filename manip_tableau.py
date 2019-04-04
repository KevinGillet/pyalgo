"""
@name manip_tableau.py
@author Aélion
@version 1.0.0
Algorithmique spécifique sur les collections
"""
"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if (firstVal < secondVal):
        return firstVal
    else:
        return secondVal

"""
getHigherOf function
return the highest value of two params
"""
def getHigherOf(firstVal, secondVal):
    if (firstVal > secondVal):
        return firstVal
    else:
        return secondVal

"""
compare function
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Chosen way to compare
@return greater or lower value of two depeding on howTo
"""
"""
def compare(firstVal, secondVal, howTo):
    if howTo == "lower":
        if (firstVal < secondVal):
            return firstVal
        else:
            return secondVal
    if howTo == "greater":
        if (firstVal > secondVal):
            return firstVal
        else:
            return secondVal
    else:
        print("Error")
"""

"""
Autre solution
"""
def compare(firstVal, secondVal, desc=True):
    if desc:
        return getLowerOf(firstVal, secondVal)
    return getHigherOf(firstVal, secondVal)

"""
min function
@param anArray The array from which I wat to get the min value
@return the min value of anArray
"""
def min(anArray):
    theMin = anArray[0]
    for value in anArray[1:]:
        theMin = compare(theMin, value)

    return theMin

"""
max function
@param anArray The array from which I want to get the max value
@return the max value of anArray
"""
def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax, value, desc=False)

    return theMax

"""
average function
@param anArray The array from which I want to get the average
@return The average of anArray
"""
def average(anArray):
    total = 0
    lengthArray = 0
    for val in anArray[:]:
        total = total + val
        lengthArray += 1
    return total / lengthArray

"""
factorial function
@param anArray The array from which I want to get the factorial
@return The factorial of anArray
"""
def factorial(anArray):
    fact = 1
    for val in anArray:
        fact = fact * val
    return fact

#Déclaration du tableau
monTablo = [15, 3, 25, 12, 7, -15]
monAutreTablo = [21, 17, -8, 65, -20, 7]

#print("Compare (lower):", compare(5, 3))
#print("Compare (greater):", compare(5, 3, desc=False))

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
    minValue = getLowerOf(minValue, monTablo[indice])
print(minValue)

print(min(monTablo))

#Print maximum value of array
print("Maximum value from array:")
maxValue = monTablo[0]
for indice in range(1,len(monTablo)):
    maxValue = getHigherOf(maxValue, monTablo[indice])
print(maxValue)

print(max(monTablo))

#Print sum of array values
print("Sum of array values:")
sumArray = 0
for indice in range(len(monTablo)):
    sumArray = sumArray + monTablo[indice]
print(sumArray)

#Average of an array
print("Average of the array:\n", average(monTablo))
#print((15+3+25+12+7-15)/6)
print("Average of the other array:\n", average(monAutreTablo))
#print((21+17+-8+65+-20+7)/6)

#Factorial of an array
print("Factorial of the array:\n", factorial(monTablo))
print(15*3*25*12*7*-15)

#Sort array by increasing order
print("Array sorted by increasing order:")

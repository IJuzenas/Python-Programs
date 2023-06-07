primeNumbers = [2, 3, 5, 7, 11]
print(type(primeNumbers))
names = ['Ignas', 'Vladas', 'Kristupas']
primeAndPeople = ['Ignas', 11, 3, 'Vladas']

newList = primeNumbers + names
print(newList)

primeNumbers = [2, 3, 5, 7, 11]
print (primeNumbers[2])

bestPrime = primeNumbers[4]
print(bestPrime)

#Add numbers to list
primeNumbers.append(13)
print(primeNumbers)

#Remove number from the list
primeNumbers.remove(5)
print(primeNumbers)

#Clear all from the list
primeNumbers.clear()
print(primeNumbers)
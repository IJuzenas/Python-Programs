#Tuples
tuple1 = (5, 10, 'softlinks', 4.5)
print(tuple1)

#Find the possition of element in tuple
print(tuple1.index(4.5)) 

print(tuple1.count(10))

tupeToList = list(tuple1)
num = [1,2,3]
listTuple = tuple(num)

print(type(tupeToList))
print(type(listTuple))
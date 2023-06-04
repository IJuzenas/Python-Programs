message1 = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t." '
print(message1)

#Multiline Strings
message2 = '''He said, "Aren't can't shouldn't wouldn't." '''
print(message2)

#Multiplying Strings
print('Python ' * 3)

#Using placeholders in String
myAge = 20
myName = 'My name is Ignas'
myMessage = '%s I am %s years old'
print (myMessage % (myName, myAge))

#F String
myAge = 20 + 5 
myName = 'My name is Ignas'
myMessage = f'{myName} I am {5*5} years old'
print (myMessage)

#len function - counts chars
txt = 'Welcome to Softlinks'
print (txt.upper())
print(txt.lower())
print(txt.count('o'))
print(txt.index('i'))
print(txt.replace('o', 'i'))
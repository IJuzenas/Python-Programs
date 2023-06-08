for x in range (0,5):
    print (f'Hello {x}') #Formatted string

names = ('Adam', 'Ignas', 'Sam')

for x in names:
    print(f"Hello {x}")
    
num = 5
#while loop
while num < 10:
    num = num +1
    print ('My endless loop')
    
#Nested loops (loop inside loop)
items = [['red', 'pink'], ['berry', 'grapes'], ['cat', 'dog']]

for item in items:
    for x in item:
        print(x)  

#TASK 
for x in range (1, 11):
    for y in range (1, 13):
        print (f'{x} x {y} = {x*y}')           
    print('=============')    
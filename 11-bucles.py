numbers = [1,2,3,4,5,6]

for numero in numbers:
    print(numero)

fruits = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate']
for fruit in fruits:
    if fruit == 'Naranja':
        print('Naranja encontrada')

x = 0
while x < 5:
    if x == 1:
        print('X es 1')
        x+=1
        continue #pasa a la siguiente iteracion y ya no evalua lo de abajo
    if x == 2:
        print('X es 2')
        break #acaba el bucle
    print(x) 
    x+=1
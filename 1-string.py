nombre = 'Mario'
apellido = 'Arango'
nombre_completo = nombre + ' ' + apellido

saludo = 'Hola ' + nombre_completo
texto = '''Hola
me llamo 'Mario' y estoy aprendiendo Python'''

print(saludo)

#Funcion, son globales y se llaman directamente, operan con argumentos
#Metodos, estan asociadas a un objeto, se definen dentro de una clase

print(nombre.upper())
print(nombre.lower())
print('mario arango'.title())
print('mario arango'.capitalize())
print('mario arango'.split(' '))
print('mario arango'.replace(' ', '|'))
print('mario arango'.count('a'))
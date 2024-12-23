diccionario = {
    'nombre': 'Mario',
    'apellido': 'Arango',
    'edad': 29,
    'profesion': {
        'carrera': 'Sistemas',
        'trabajo': 'desarrollador'
    }
}
del diccionario['edad']

print(diccionario['profesion']['carrera'])
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())


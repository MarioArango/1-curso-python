numbers = list(range(1, 21))
print(numbers)

#spread operator en listas, nueva lista, copia de primer nivel
numbers_edit = [*numbers]
print(numbers_edit)

persons = [
    {
        'id': 1,
        'name': 'Mario',
        'age': 29,
        'genre': 'M'
    },
    {
        'id': 2,
        'name': 'Clara',
        'age': 26,
        'genre': 'F'
    },
    {
        'id': 3,
        'name': 'Diego',
        'age': 17,
        'genre': 'M'
    }
]

#spreed operator en diccionarios, copia superficial de primer nivel
#Mas pythonico son las list compresions y sirven para hacer map y filter
persons_edit = [
    {
        **person,
        'age': 'Mayor' if person['age'] >= 18 else 'Menor',
        'genre': 'Masculino' if person['genre'] == 'M' else 'Femenino'
    } if person['id'] == 2 else person #validacion de edicion o transformacion -> map()
    for person in persons
    if person['id'] == 1 #validacion de filtro -> filter()
    if person['age'] == 18 # enves de and para ser facil de comentar y ser mas ordenado
]
print(persons_edit)

# persons_edit_map = list(map(lambda person: {
#     **person,
#     'age': 'Mayor' if person['age'] >= 18 else 'Menor',
#     'genre': 'Masculino' if person['genre'] == 'M' else 'Femenino'
# }, persons))

# print(persons_edit_map)

#busca y el primero que cumpla lo trae, sino trae el segundo argumento
find_mario = next((person for person in persons if person['name'] == 'Mario') , '-')
print(find_mario)

#busca el valor de la key y si no existe trae el segundo parametro
person = {
    'id': 3,
    'name': 'Diego',
    'age': 17,
    'genre': 'M'
    }
name = person.get('name', '-')
print(name)

#en operadores ternarios es if else, no existe elif
age = 'Mayor' if person['age'] > 18 else 'Menor' if person['age'] < 18 else 'Intermedio'
print(age)
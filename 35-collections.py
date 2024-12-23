from collections import defaultdict
from time import time

#Nunca genera error KeyError, es decir que si intentamos acceder a un key que no existe, 
#retornara el valor por defecto natural o peronalizado definido en el defaultdict
#Suelen ursarse para ocurrencias y agrupamientos

#1. default con int por defecto, el valor por defectode int es 0
fruits = ['manzana', 'naranja', 'manzana', 'pera', 'naranja']
contador = defaultdict(int) # contador = {} cuyos values por defecto seran 0
print(contador['naranja']) # es un diccionario vacio, y no da error, retorna 0

for fruit in fruits:
    contador[fruit] += 1
print(contador)

#2. Agrupamiento
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4)]
groups = defaultdict(list) # el valor por defecto de list es []
# print(groups['hola']) #retorna [], porque no existe

for key, value in data:
    groups[key].append(value)
print(groups)

#3. con un valor por defecto personalizado
custom_list = defaultdict(lambda: 'Sin informacion') # custom str por defecto
custom_list['alumno'] = 'Mario'
print(custom_list['alumno']) # como ya lo cree, retorna Mario
print(custom_list['hola']) # como no existe, retorna el defecto "Sin informacion"

#MÁS EJEMPLOS

#1. Agrupamiento: Agrupar acciones de usuario, analizar registros de acceso y agrupar por usuario
logs = [
    ('usuario1', 'login'),
    ('usuario2', 'logout'),
    ('usuario1', 'view_page'),
    ('usuario2', 'login')
]

actions_user = defaultdict(list)
for key, value in logs:
    actions_user[key].append(value)

print(actions_user.items()) #nos devuelve la lista de diccionarios creada, que es un iterable

for user, action in actions_user.items():
    print(user, action)

#2. AGRUPAMIENTO, calificaciones

print('------------------------------------------------------')

califications= [
    ("Ana", "Matemáticas", 90),
    ("Juan", "Historia", 85),
    ("Ana", "Historia", 88),
    ("Pedro", "Matemáticas", 75),
    ("Ana", "Ciencias", 92)
]

groups_califications = defaultdict(list)

#transforma el diccionario en una lista de tuplas, (key, value) para ser recorrida
for student, materia, calification in califications:
    groups_califications[student].append((materia, calification))

for key, value in groups_califications.items():
    print(key, value)

# SI NO EXISTE LO CREA, por eso es mejor usar get en caso sea consulta
print(groups_califications['hola']) 

 #Por eso en caso sea consulta, es mejor usar get, porque no creara, si no existe retorna None oel valor por defecto especificado
print(groups_califications.get('hola', [])) #como el default list es un list, le pongo un []

#retorna el diccionario creado
print(dict(groups_califications))

#asi tambien se puede validar su existencia
print('hola' in groups_califications)

print('------------------------------------------------------')

# #3. OCURRENCIAS, de palabras repetidas
text = "el gato y el perro corrian el gato salto"
repetitions = defaultdict(int)

for value in text.split():
    repetitions[value] += 1

print(dict(repetitions))

print('------------------------------------------------------')

# EJEMPLOS DE CASOS DE USO REALES

#1. Contador de votos en una eleccion, OCURRENCIAS
resultados = ['candidatoA', 'candidatoB', 'candidatoA', 'candidatoC', 'candidatoA']
votos = defaultdict(int)
for voto in resultados:
    votos[voto] += 1
print(dict(votos))

print('------------------------------------------------------')

#2. Registro de temperaturas de la ciudad, AGRUPAMIENTO
registros = [
    ('Madrid', 20), 
    ('Barcelona', 22), 
    ('Madrid', 19), 
    ('Barcelona', 23), 
    ('Valencia', 25)
]

temperaturas = defaultdict(list)
for ciudad, temperatura in registros:
    temperaturas[ciudad].append(temperatura)
print(dict(temperaturas))

print('------------------------------------------------------')

#3. Estado de tareas con valor por defecto
tareas = defaultdict(lambda: 'Pendiente')
tareas['Proyecto A'] = 'Completado'
tareas['Proyecto B'] = 'En progreso'
print(tareas.get('Proyecto C')) #consulta
print(tareas['Proyecto C']) #consulta, y si no existe lo crea con el valor por defeto "Pendiente"
print(dict(tareas))

print('------------------------------------------------------')

#4. Registro de errores por severidad, AGRUPAMIENTO DOBLE
logs_errors = [
    ('ERROR', 'login', 'credenciales inválidas'),
    ('WARNING', 'database', 'conexión lenta'),
    ('ERROR', 'login', 'timeout')
]

# seras un diccionario, tus keys seran otro diccionario con keys de listas
groups_errors = defaultdict(lambda: defaultdict(list))
for error, module, message in logs_errors:
    groups_errors[error][module].append(message)

print('ERORR:', dict(dict(groups_errors)['ERROR']))

for error, suberror in groups_errors.items():
    print(error)
    for module, message in suberror.items():
        print(module, message)

print('------------------------------------------------------')

#5. Gestion de inventario por categoria y producto, AGRUPAMIENTO Y OCURRENCIA
movimientos = [
    ('Electrónica', 'Laptop', 5),
    ('Ropa', 'Camiseta', 10),
    ('Electrónica', 'Laptop', -2),
    ('Ropa', 'Pantalón', 8)
]
inventario = defaultdict(lambda: defaultdict(int))
for category, device, stock in movimientos:
    inventario[category][device] += stock
print(inventario)

print('------------------------------------------------------')

#6. Sistema de cache con tiempo de expiracion
cache = defaultdict(lambda: {'valor': None, 'expira': 0})
def save_in_cache(key, value, time_expiration = 60):
    cache[key] = {'valor': value, 'expira': time() + time_expiration}

save_in_cache('usuario_1', 'Mario', 40)
print(dict(cache))

print('------------------------------------------------------')

#7. Arbol de categorias anidadas
products = [
    ('Electrónica', 'Computadoras', 'Gaming', 'PC Gamer'),
    ('Electrónica', 'Computadoras', 'Oficina', 'Laptop'),
    ('Ropa', 'Hombre', 'Casual', 'Camiseta')
]
#si hay 3 defaultdict, es que hay 2 niveles dentro
categories = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
for category, subcategory, type, product in products:
    categories[category][subcategory][type].append(product)

print(dict(categories))

print('------------------------------------------------------')

#8. Sistema de permisos por rol y recurso
acciones = [
    ('admin', 'usuarios', 'crear'),
    ('admin', 'usuarios', 'eliminar'),
    ('usuario', 'documentos', 'leer')
]
permisos = defaultdict(lambda: defaultdict(list))
for rol, user, action in acciones:
    permisos[rol][user].append(action)
print(dict(permisos))

print('------------------------------------------------------')

# 10. Sistema de eventos con callbacks
eventos = defaultdict(lambda: defaultdict(list))

def registrar_evento(evento, fase, callback):
    eventos[evento][fase].append(callback)

def evento_ejemplo():
    print("Ejecutando evento")

registrar_evento('login', 'antes', lambda: print("Verificando credenciales"))
registrar_evento('login', 'después', lambda: print("Registrando acceso"))
print("\n10. Sistema de eventos:", {k: dict(v) for k, v in eventos.items()})
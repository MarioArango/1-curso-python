# kwargs es un diccionario, **kwargs es la desestructuracion del diccionario, por eso permite pasar
# parametros con nombre"clave valor", key word arguments
def imprimir_datos(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Puedes llamarla con cualquier cantidad de argumentos nombrados
# imprimir_datos(nombre="Juan", edad=30)
# imprimir_datos(ciudad="Madrid", pais="España", codigo_postal="28001")

data = {
    'nombre': 'mario',
    'edad': 29
}

def saludar(nombre, edad):
    print(f'Hola {nombre}, tienes {edad} años')

saludar(**data)

#args es una tupla, *args es un conjunto de parametros separados con coma "," como la definicion de una tupla
#como debajo trabajamos con args, estamos trabajando con una tupla
def suma(*args):
    print(args)
    print(type(args))
    total = 0
    for numero in args:
        total += numero
    return total

# Puedes llamarla con cualquier cantidad de argumentos
print(suma(1, 2))  # 3
print(suma(1, 2, 3, 4, 5))  # 15
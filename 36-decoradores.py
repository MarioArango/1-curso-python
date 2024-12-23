import time
# Se basa en que las funciones son objetos de primera clase y por ende pueden ser pasados como parametros en otras funciones
#Evita el DRY
#Separa funcionalidades transversales como loggin, permisos
'''
    Sirve para :
        Modificar el comportamiento de funciones o clases
        Añadir funcionalidad adicional
        Validar entradas
        Medir rendimiento
        Implementar patrones de diseño
        Gestionar permisos y roles
        Cachear resultados
'''
'''
    Cuando se usan:
        Se quiere añadir comportamiento comun en multiples funciones
        Validar o modificar argumentos
        Registrar informacion sobre la ejecucion
        Verificar precondiciones
        Gestionar recursos
'''
#1. Decorador sin argumentos

def mi_decorador(fun):
    def wrapper():
        print('Antes de la ejecucion')
        fun()
        print('Despues de la funcion')
    return wrapper

#decorador + funcion es equivalente a wrapper, por eso cuando se ejecuta saludo es como ejecutra wrapper
@mi_decorador
def saludo():
    print('Hola')

saludo()

print('-------------------------------------------')

#Decorador que acepta argumentos en la funcion
def decorador_args(fun):
    def wrapper(*a, **b):
        print('Inicio')
        print(a)
        print(type(a))
        print(b)
        print(type(b))
        fun(*a, **b)
        print('Final')
    return wrapper

@decorador_args
def suma(a, b, c):
    print(a + b + c)

suma(1, 2, c = 3) #(1,2), {'c': 3}

# print('-------------------------------')
#args es una tupla, *args es un conjunto de parametros separados con coma "," como la definicion de una tupla
#como debajo trabajamos con args, estamos trabajando con una tupla
# def suma(*args):
#     print(args)
#     print(type(args))
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# Puedes llamarla con cualquier cantidad de argumentos
# print(suma(1, 2))  # 3
# print(suma(1, 2, 3, 4, 5))  # 15

# print('-------------------------------')

#kwargs es un diccionario,  **kwargs es la desestructuracion del diccionario, por eso permite pasar
# parametros con nombre"clave valor", key word arguments
# def imprimir_datos(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# Puedes llamarla con cualquier cantidad de argumentos nombrados
# imprimir_datos(nombre="Juan", edad=30)
# imprimir_datos(ciudad="Madrid", pais="España", codigo_postal="28001")

print('-------------------------------')

#3. Decorador para medir tiempos de ejecucion
def medir_tiempo(fun):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = fun(*args, **kwargs)
        fin = time.time()
        print(f'Tiempo de ejecucion: {fin - inicio:.4f}seg')
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    time.sleep(2)
    return 'operacion completa'

operacion_lenta()

print('-------------------------------')

#4 Decoradores con parametros
def decorador_personalizado(user): #parametros del decorador
    print(f'{user} inicio ejecucion') #se puede hacer algun tipo de validacion
    def decorador(fun): #para abajo lo mismo
        def wrapper(*args, **kwargs):
            print('inicio')
            resultado = fun(*args, **kwargs)
            print('fin')
            return resultado
        return wrapper
    return decorador

@decorador_personalizado('marango')
def saludar_usuario(nombre):
    return f'Hola {nombre}'

saludar_usuario('Mario')

#5. Decorador para cachear resultados

print(('1','2') in {'1': 'hola', '2': 'mario'})
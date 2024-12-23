#Variable local, solo existe en su bloque
#Variable global, en todo

#Como en python no hay tipo de variables como let o const
#cada declaracion de la variable en un bloque es una nueva variable
#con su referencia de memoria diferente, para decirle a python que esta
#no sera una nueva variable sino una ya definida anteriormente en un nivel superior
# se usa los prefijos global o nonlocal

# x = 100 #variable global

# def local_function():
#     #Declara una nueva variable x, solo que no tiene let o const
#     x = 10 #variable local
#     print(f'El valor de la variable es {x}')

# def show_global():
#     print(f'El valor de la variable global es {x}')

# local_function()
# show_global()

#Puede estar declarada al inicio o mas abajo, pero es buena practica al inicio
#En python primero declaras y luego consumes, no hay hoisting
#Se considera global porque esta declarada a nivel de archivo o modulo y con la sangria inicial

# def outer_function():
#     #declara una "nueva" variable local o por ser intermedio enclosing scope, 
#     # que casualmente tiene el mismo nombre que la global
#     x = 'enclosing' #como es un intermedio se le llama ENCLOSING SCOPE
#     x = 'hola' #mismo x
#     for i in [1,2,3]:
#         x = i #mismo x

#     # En Python, los nuevos scopes para variables se crean a nivel de funciones
#     def inner_function(): #CREA UNA UNEVO SCOPE
#         #"DECLARA" una nueva variable local
#         global x #busca la variable global sin sangria a niel de archivo, declarada más arriba
#         x = 'local'
#         print(x)

#     inner_function() #local
#     print(x) #enclosing

# def other_function():
#     print(x)

# outer_function()
# other_function() #funciona porque la funcion aterior ya la creo
# print(x)

#global te permite acceder y modificar (o crear si no existe) una variable en el scope global
#nonlocal te permite acceder y modificar (pero no crear) una variable en el scope intermedio más cercano

def outer_function():
    x = 'enclosing'  # Variable en scope intermedio
    
    def inner_function():
        nonlocal x  # Indica que queremos modificar la x del scope inmediatamente superior
        x = 'modificado'  # Modifica la x de outer_function
        print(x)  # modificado
    
    inner_function()
    print(x)  # modificado

outer_function()

# Se usa dentro de funciones anidadas
# Busca la variable en el scope inmediatamente superior (enclosing scope)
# A diferencia de global, no puede crear la variable si no existe

#1ER CASO NO POSIBLE
# En el primer caso DA ERROR, porque no existe una variable x en el scope superior
# def outer_function():
#     def inner_function():
#         nonlocal x # Esto dará error porque x no existe en el scope superior
#         x = 'modificado'

# 2DO CASO NO POSIBLE
# En el segundo caso, nonlocal no puede acceder directamente al scope global

# x = 'global'

# def function():
#     nonlocal x  # Esto dará error porque nonlocal no puede acceder al scope global
#     x = 'modificado'

#nonlocal solo sirve para SCOPE ENCLOSING
# nonlocal es específicamente para trabajar con variables en el scope enclosing (scope envolvente o intermedio).
#Necesita que exista al menos un scope intermedio

# def outer_function():
#     x = 'enclosing'  # Esta es una variable en scope enclosing
    
#     def inner_function():
#         nonlocal x   # Solo puede afectar a variables en scope enclosing
#         x = 'modificado'
        
#         def deepest_function():
#             nonlocal x  # También puede acceder al scope enclosing desde más niveles de profundidad
#             x = 'modificado desde más adentro'
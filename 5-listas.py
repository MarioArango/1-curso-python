to_do = ['Dirigirnos al hotel', 'Ir a almorzar', 'Visitar un museo', 'Volver al hotel']
print(type(to_do))

numbers = [1,2,3,4,5]
print(type(numbers))

print(len(numbers))
print(numbers[0])

cadena ='Hola mundo'
print(cadena[4:7])
to_do.append(False)
to_do.insert(0, 'Nueva informacion')
print(to_do)
print(to_do.index('Ir a almorzar'))
print(max(numbers))
print(min(numbers))

del numbers[0]
print(numbers)
del numbers[0:2]
print(numbers)

#del numbers elimina todo como un garbage collector

#La igualdad ve los items, para ver las ref de memoria se usa is

#efecto de lado de la original
lista_edades = [21, 22, 23, 24]
nueva_lista_edades = lista_edades 

#si efecto de lado
nueva_lista_edades_2 = lista_edades[:]
nueva_lista_edades_3 = lista_edades.copy()

print(id(lista_edades))
print(id(nueva_lista_edades))
print(id(nueva_lista_edades_2))
print(id(nueva_lista_edades_3))
print(lista_edades == nueva_lista_edades_3)
print(lista_edades is nueva_lista_edades_3)

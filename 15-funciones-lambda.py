#Es una funcion anonima

add = lambda a, b: a + b
print(add(1, 2))

#funcion map, un iterador necesita ser envuelto en list
#Esto es asi porque se aplica LAZY EVALUATION, iteradores, por tema de eficiencia
#Por lo que si quieres usar un item es a demanda o usando la funcion list
#Puede recorrer listas o iterables

numbers = [x for x in range(11)]
print(numbers)
numbers_squared = list(map(lambda x: x**2, numbers))
print(numbers_squared)
numbers_sum = list(map(lambda x, y : x + y, numbers, numbers_squared))
print(numbers_sum)
numbers_par = list(filter(lambda x: x%2 == 0, numbers_sum))
print(numbers_par)
#Sirve para recorrer sin el index los items de una lista

numbers  = [1,2,3,4]
numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

nombre = 'Mario'
nombre_iterator = iter(nombre)
print(next(nombre_iterator))
print(next(nombre_iterator))

limit = 10
fruits = range(1,limit + 1,2)
fruits_iterable = iter(fruits)
print(next(fruits_iterable))
print(next(fruits_iterable))
print(next(fruits_iterable))
print(next(fruits_iterable))
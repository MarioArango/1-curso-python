#Los generadores ya son iteradores por naturaleza, por lo que no necesitan la funcion iter
#Suelen usarse para grandes listas de modo que se requiera valores bajo demanda

def generator_numbers():
    yield 1
    yield 2
    yield 3
    yield 4

#1. Forma de recorrer sus valores
for number in generator_numbers():
    print(number)

#2. Forma de transformarlo a una lista, no seria conveniente si es una lista infinita, error memoria
print(list(generator_numbers()))

#3. Como son iteradores por defecto ya no necesitan la funcion iter, defrente se puede obtener sus valores con next
numbers = generator_numbers()
print(next(numbers))
print(next(numbers))
print(next(numbers))

#Ejemplo real de una lista con numeros pares infinitos
#Si fuera una lista habria desbordamiento de memoria

#Aca el define que sera infinito, pero no guarda nada, y los valores los obtiene bajo demanda
def generator_pares_infinitos():
    number = 0
    while True: #El while es como crear varios bloques de codigo con yields estaticos, pero al ejecutar se acuerda en donde esta y los estados
        yield number
        number += 2

numbers_pares = generator_pares_infinitos() #Se trabaja asi para mantener la misma ref en memoria
for number in numbers_pares:
    print(number)
    if number == 20:
        break

#Ejemplo real Fibonnaci(porque se aplica aca?, porque fibonacci es infinito)
def generator_fibonnaci():
    next_number = 1
    prev_number = 0

    yield prev_number
    yield next_number

    while True:
        current_number = prev_number + next_number
        yield current_number
        prev_number = next_number
        next_number = current_number
#0 1 1 2 3 5 8

numbers_finanacci = generator_fibonnaci()
for number in numbers_finanacci:
    print(number)
    if number > 20:
        break
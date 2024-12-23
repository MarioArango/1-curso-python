# List compresions
lista = [ x**2 for x in range(1,11) ]
print(lista)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [ (temp*9/5)*32 for temp in celsius ]
print(fahrenheit)

#range es un objeto iterable
x = range(0,11)
print(x) #objeto iterable
print(list(x)) #funcion list genera una lista de un objeto iterable

#Numeros pares
evens = [ x for x in range(1, 21) if x%2 == 0]
print(evens)

#Transpuesta de una matris
matris = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matris)

transpuesta = [ [row[i] for row in matris] for i in range(len(matris[0])) ]
print(transpuesta)
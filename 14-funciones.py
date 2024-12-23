def greet(name, lastname):
    print(f'Hola {name} {lastname}')

greet('Mario', 'Arango')

#Parametros posicionales
greet(lastname='Arango', name='Mario') #Sirve para no hacer el patron duck

#CALCULADORA
def suma(a, b):
    return a + b

def resta(a, b):
        return a - b

def multiplicacion(a, b):
     return a*b

def division(a,b):
     return a/b

def calculadora():
    number_opcion = int(input('''
    Que desea realizar:
        Sumar: 1 
        Restar: 2 
        Multiplicar: 3 
        Dividir: 4
        Salir: 5
    '''))

    a = float(input('Ingrese un numero: '))
    b = float(input('Ingrese otro numero: '))

    result = 0

    if number_opcion == 1:
         result = suma(a,b)
    if number_opcion == 2:
         result = resta(a,b)
    if number_opcion == 3:
         result = multiplicacion(a,b)
    if number_opcion == 4:
         result = division(a,b)
    
    if number_opcion == 5:
         print('Finalizado')
    else:
         print(f'El resultado es: {result}')
         calculadora()

calculadora()
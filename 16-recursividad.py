#Funciones que se llman a si misma, debe haber una validacion para no generar una ejecucion infinita

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
factorial_n = factorial(4)
print(factorial_n)

def fibonacci(index):
    if index < 0:
        return 0
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)
    
#0 1 1 2 3 5 8
fibonacci_n = fibonacci(6)
print(fibonacci_n)
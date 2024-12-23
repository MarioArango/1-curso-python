import multiprocessing

#Funcion que calcule el cuadrado de un numero
def calculate_square(n):
    return n*n

if __name__ == '__main__':

    numbers = [1,2,3,4,5]

    #Crear un pool (procesos independientes con sus hilos principales, al final serian procesos hijos del proceso principal de python, cuyo resultado se unira al final al proceso principal)
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)
        print(f'Resultados: {results}')

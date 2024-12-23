from multiprocessing import Pool

#Procesamiento en paralelo de una lista de numeros
def calcular_cuadrado(numero):
    return numero*numero

if __name__ == '__main__':
    numeros = range(1, 11)
    procesos = []

    #Crear pool de "4" procesos
    #Pool es un conjunto de nucleos - hilos - ejecuciones
    with Pool(processes=4) as pool:
        resultados = pool.map(calcular_cuadrado, numeros)
        print(f'Cuadrados: {resultados}')
    #[1,2,3,4,5,6,7,8,9,10] cada nucleo se encarga de resolver alguno de ellos
    #talvez el proceso1: 1**2 y 2**2
    #talvez el proceso2: 3**2 y 4**2
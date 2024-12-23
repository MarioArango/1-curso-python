from multiprocessing import Process

def saludar(nombre):
    print(f'Hola {nombre}')

if __name__ == '__main__':
    #Crear procesos 'hilos' para saludar a diferentes personas
    nombres = ['Ana', 'Juan', 'Maria', 'Carlos']
    procesos = []

    for nombre in nombres:
        p = Process(target=saludar, args=(nombre,))
        procesos.append(p)
        p.start()

    #Esperar que todos los procesos terminen para unirlo al proceso principal
    for proceso in procesos:
        proceso.join()
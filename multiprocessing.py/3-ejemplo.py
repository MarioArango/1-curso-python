from multiprocessing import Process, Queue
import time
#Comunicacion entre procesos

def productor(queue):
    for i in range(5):
        mensaje = f'Mensaje {i + 1}'
        queue.put(mensaje)
    queue.put(None) #Señal de terminacion

def consumidor(queue):
    while True:
        print('antes')
        mensaje = queue.get()
        print('--', mensaje)
        if mensaje is None:
            break
        print(f'Recibido: {mensaje}')

if __name__ == '__main__':
    queue = Queue()
    #Crear procesos productor y consumidor
    prod = Process(target=productor, args=(queue,))
    cons = Process(target=consumidor, args=(queue,))

    prod.start()
    cons.start()

    prod.join()
    cons.join()
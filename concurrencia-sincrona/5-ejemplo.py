import threading
import queue
import time

'''
EJEMPLO 4: Cola de Mensajes (Queue)
---------------------------------
CASO DE USO:
- Sistemas de procesamiento de tareas en background
- Arquitecturas productor-consumidor
- Sistemas de mensajería y procesamiento de eventos

CUÁNDO USAR:
- Cuando necesitas comunicación thread-safe entre threads
- Para implementar sistemas de colas de trabajo
- Cuando quieres desacoplar la producción del consumo de datos

POR QUÉ QUEUE:
- Proporciona comunicación thread-safe
- Permite el procesamiento asíncrono de tareas
- Ideal para balancear cargas de trabajo
'''
def productor(cola: queue.Queue):
    for i in range(3):
        mensaje = f'Mensaje {i + 1}'
        time.sleep(1) # pausar y ejecutar otro hilo
        cola.put(mensaje)
        print(f'{mensaje} producido')

'''
El get() actúa como un punto de sincronización natural entre los hilos, sin necesidad de time.sleep(). 
Es como una "pausa automática" que:
    No desperdicia CPU
    Se desbloquea inmediatamente cuando hay datos
    Maneja la sincronización internamente
'''

'''
get_nowait() es una versión no bloqueante de get(). La diferencia principal es:
get():
    Bloquea el hilo hasta que haya un elemento disponible
    Espera indefinidamente si la cola está vacía
get_nowait():
    No bloquea el hilo
    Lanza una excepción queue.Empty si la cola está vacía
    Es equivalente a get(block=False)
'''
def consumidor(cola: queue.Queue):
    while True:
        # print('primero: ', cola.get())
        mensaje = cola.get()
        if mensaje is None:
            break
        print(f'{mensaje} fue consumido')
        cola.task_done()
    
cola_compartida = queue.Queue()

thread_productor = threading.Thread(target=productor, args=(cola_compartida,))
thread_consumidor = threading.Thread(target=consumidor, args=(cola_compartida,))

thread_productor.start()
thread_consumidor.start()

thread_productor.join()
cola_compartida.put(None) #Señal de finalización
thread_consumidor.join()
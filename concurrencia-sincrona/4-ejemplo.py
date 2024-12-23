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

def productor(cola_compartida):
    for i in range(3):
        mensaje = f'Mensaje {i + 1}'
        cola_compartida.put(mensaje)
        print(f'{mensaje} fue guardado en la cola')
        time.sleep(1) #al puasar pasa al otro hilo

def consumidor(cola_compartida):
    for i in range(3):
        mensaje = cola_compartida.get()
        print(f'{mensaje} fue consumido')
        time.sleep(1) #al puasar pasa al otro hilo

#Espacio en memoria RAM que almacena datos (put) siguiendo el principio FIFO (get), cola seguro que mantiene la sincronia automaticamente
cola_compartida = queue.Queue()

thread_productor = threading.Thread(target=productor, args=(cola_compartida,))
thread_consumidor = threading.Thread(target=consumidor, args=(cola_compartida,))

thread_productor.start()
thread_consumidor.start()

thread_productor.join()
thread_consumidor.join()



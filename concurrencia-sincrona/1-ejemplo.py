import threading
import time

#Trea o funcion a ejecutar en un nuevo hilo de forma concurrente
def print_message_thread(id):
    #-------------------------------BLOQUE 1-----------------------------------
    #Obtenemos el nombre del hilo donde se esta ejecutando esta tarea, 
    current_name_thread = threading.current_thread().name

    #Ejecutamos la primera tarea
    print(f'Ejecutando desde el thread {id}: {current_name_thread}')
    
    #Dormimos la tarea en su hilo por 2 segundos, por lo que el GIL pasaria a la ejecucion de otra tarea en otro hilo
    #la concurrencia se da entre hilos ejecutando el bloque 1 y 2
    time.sleep(2)

    #-------------------------------BLOQUE 2-----------------------------------
    #Una vez finalizada ejecuta esto
    print(f'Thread {id}: {current_name_thread} ha finalizado')

#creamos el primer hilo
first_thread_created = threading.Thread(target=print_message_thread, args=(1,))
#creamos el segundo hilo
second_thread_created = threading.Thread(target=print_message_thread, args=(2,))

#iniciar ejecucion de la primera tarea el el hilo creado
first_thread_created.start()
#iniciar ejecucion de la segunda tarea el el hilo creado
second_thread_created.start()

#uni la respuesta al hilo principal de python
first_thread_created.join()
second_thread_created.join()

#Cosas que podria mejorar: como la creacion, el inicio y la union al hilo principal, son repetidas, lo podria generalizar
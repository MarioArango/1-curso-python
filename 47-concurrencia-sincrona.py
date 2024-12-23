# Puede ser en un nucleo - hilo (asyncio.gather - asincrono) 
# o en varios nucleos - hilos (threands - sincrono bloqueante - para libs que no soportan asincronismo - no para tareas de cpu intensivas)

#PROCESO SINCRONO BLOQUEANTE, POR ESO TRABAJAREMOS CON CONCURRENCIA EN MULTIPLES HILOS
import threading
import time

#funcion que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} completada')

threands = []

for i in range(3):
    #Crear nuevo hilo que ejecutara la funcion
    thread = threading.Thread(target=process_request, args=(i,))
    threands.append(thread)
    thread.start()

#Esperar a que todos los hilos terminen
for thread in threands:
    #Hace que el resultado se una al hilo principal
    thread.join()

print('Todas las solicitudes fueron completadas')
import threading
import time

def saludar(name):
    print(f'Iniciando tarea {name}')
    time.sleep(2)
    print(f'Tarea completada {name}')

#Generalizamos
threands = []
for i in range(1, 4):
    #Creamos
    threand = threading.Thread(target=saludar, args=(i,))
    #Ejecutamos
    threand.start()
    threands.append(threand)

for threand in threands:
    #Unimos los resultados al hilo principal
    threand.join()
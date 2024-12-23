import threading
import time
#Cuando hay un estado compartido entre hilos de ejecucion, se debe usar lock, para garantizar la actualizacion correcta
#LOCK es un candado que permite que impide que otro hilo ejecute un codigo porque otro hilo lo esta usando
#Esto hace que exista un orden en la ejecucion y no falle la actualizacion de de variables compartidas "podria estar la variable en cache l3"
'''
EJEMPLO 3: Sincronización con Lock
--------------------------------
CASO DE USO:
- Acceso a recursos compartidos (bases de datos, archivos, variables globales)
- Actualización de contadores o estadísticas compartidas
- Escritura en archivos de log compartidos

CUÁNDO USAR:
- Cuando múltiples threads necesitan modificar un recurso compartido
- Para prevenir condiciones de carrera
- Cuando necesitas garantizar la integridad de los datos

POR QUÉ THREADING CON LOCK:
- Previene corrupcción de datos en accesos concurrentes
- Garantiza la atomicidad de las operaciones
- Necesario para mantener la consistencia en recursos compartidos
'''

print('INICIO DE EJECUCIÓN SECUENCIAL')

#====================== BLOQUE DE THREADS ======================
print('INICIO DE BLOQUE CONCURRENTE')
count = 0
lock = threading.Lock()
#tarea a ejecutar con estado compartido
def increment_count():
    global count
    with lock:
        print(f'Iniciando: {count}')
        count += 1
        print(f'En pausa: {count}')

    time.sleep(2)
    count += 1
    print(f'Finalizando: {count}')
    
threads = []
#generalizamos la creacion, ejecucion y union del hilo
for i in range(1, 4):
    thread = threading.Thread(target=increment_count)#crear
    thread.start()#ejecutar
    threads.append(thread)


#NO ES RECOMENDABLE EJECUTAR CODIGO INTERMEDIO PORQUE PUEDE PERDER EL FLUJO DE EJECUCION Y NO DAR EL RESULTADO CORRECTO
#ES MEJOR MANEJAR POR BLOQUE
# print('-------------------Intermedio--------------------')

for thread in threads:
    thread.join()#unir

print(f'-------------Finalmente: {count}--------------')
#----------------------------------------------------------------------------------------------------------------------------------------

print('CONTINUACIÓN DE EJECUCIÓN SECUENCIAL')

#Una mejora seria que el estado compartido no este libre sino en una cola compartida (hilo seguro)
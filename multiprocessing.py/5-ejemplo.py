from multiprocessing import Process, Array
import time

'''
Se usa array para compartir datos entre procesos
La memoria es compartida entre procesos
Los cambios son visibles para todos los procesos
Más eficiente en memoria (solo hay una copia)
Es thread-safe y process-safe (maneja la sincronización automáticamente)
'''

def incrementar_seccion(array_compartido, id_proceso, inicio, fin):
    '''Cada proceso incrementara sus numeros asignados en 1'''
    print(f'Proceso {id_proceso} iniciando: {inicio} hasta {fin}')
    for i in range(inicio, fin):
        valor_actual = array_compartido[i]
        array_compartido[i] = valor_actual + 1
        time.sleep(1)
    print(f'Proceso {id_proceso} termino')

if __name__ == '__main__':
    #crear un array compartido de 12 numeros
    tamaño = 12
    # 'i' significa que son enteros e inicializan en 0
    array_compartido = Array('i', 12)

    #Vamos a crear 3 procesos, cada uno manejara 4 numeros
    procesos = []
    numeros_pro_proceso = tamaño // 3

    #Inicializar el array con valores del 0 al 11
    for i in range(tamaño):
        array_compartido[i] = i

    print(f'Array inicial: {list(array_compartido)}')

    #Crear y arrancar los procesos
    for i in range(3):
        inicio = i * numeros_pro_proceso
        fin = inicio + numeros_pro_proceso

        p = Process(target=incrementar_seccion, args=(array_compartido, i, inicio, fin))
        procesos.append(p)
        p.start()

    #Esperar a que todos terminen
    for p in procesos:
        p.join()

    print(f'Array final: {list(array_compartido)}')
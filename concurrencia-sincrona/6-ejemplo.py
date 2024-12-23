'''
EJEMPLO: Eventos (Event)
------------------------
CASO DE USO:
- Coordinación de tareas basada en eventos
- Señalización entre threads
- Implementación de patrones de espera y notificación

CUÁNDO USAR:
- Para sincronizar threads basado en condiciones
- Cuando necesitas pausar threads hasta que ocurra un evento
- Para implementar patrones de señalización

POR QUÉ EVENTS:
- Mecanismo simple para señalización entre threads
- Permite espera eficiente sin polling
- Ideal para coordinación basada en eventos
'''

#CUANDO SE TRABAJA CON COLAS O EVENTOS NO SE USA SLEEP, EL GET Y WAIT PAUSAN EN AUTOMTICO

import threading
import time

#creamos el evento
evento_sincronizacion = threading.Event()

def esperar_evento():
    print(f'Esperando señal...')
    evento_sincronizacion.wait() #salta a otro hilo - 1
    print(f'¡Señal recibida!') #como ya esta activo ejecuta esto - 4

def activar_evento():
    print('Enviando señal de activacion') #ejecuta y activa - 2
    evento_sincronizacion.set() #salta a otro hilo - 3

thread_esperar = threading.Thread(target=esperar_evento)
thread_activar = threading.Thread(target=activar_evento)

thread_esperar.start()
thread_activar.start()

thread_esperar.join()
thread_activar.join()


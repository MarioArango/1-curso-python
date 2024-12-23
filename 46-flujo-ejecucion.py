#EJECUCION CONCURRENTE
'''
    No bloqueante
    Ceden el control al event loop y esperan la respuesta en el TaskQueu
    Se envian todas las solicitudes usando "import threading", y se ejecutan al mismo tiempo en el mismo hilo del nucleo del procesador
'''

#GIL (Global Interpreter Lock)
'''
El GIL (Global Interpreter Lock) es un mecanismo de bloqueo en Python que asegura que solo un hilo pueda ejecutar código Python a la vez. Es como un "token" o "permiso" que los hilos necesitan para ejecutar código Python.
Es un candado (mutex) a nivel del intérprete
Solo un hilo puede tener el GIL a la vez
Es necesario para ejecutar código Python

¿Por qué existe?
    Para hacer thread-safe la gestión de memoria de Python
    Para proteger las estructuras de datos internas de Python
    Para simplificar el garbage collector
    Fue una decisión de diseño para hacer Python más simple y seguro

¿Cuándo se libera el GIL?
    Durante operaciones I/O (lectura/escritura de archivos)
    Durante operaciones de red
    En algunas operaciones de bibliotecas en C (como NumPy)

¿Por qué multiprocessing no está afectado?
    Cada proceso tiene su propio GIL
    Los procesos son verdaderamente paralelos
    No compiten por el mismo GIL

Ventajas del GIL:
    Hace el código single-threaded más rápido
    Simplifica la implementación de C extensions
    Hace la gestión de memoria más simple y segura

Desventajas del GIL:
    Limita el verdadero paralelismo con threads
    Puede causar overhead en aplicaciones multi-thread
    No aprovecha múltiples cores para código Python puro

Cómo trabajar con el GIL:
    Usar asyncio para concurrencia en un solo hilo
    Usar multiprocessing para paralelismo real
    Usar threads solo para operaciones I/O-bound
    Usar bibliotecas como NumPy que liberan el GIL

¿Por qué no se elimina?
    Mantener compatibilidad con código existente
    La complejidad de cambiar la gestión de memoria
    Muchas C extensions dependen de él
    El beneficio no justifica el costo del cambio

Soluciones disponibles:
    Usar asyncio para concurrencia I/O
    Usar multiprocessing para cálculos intensivos CPU
    Usar bibliotecas como NumPy que liberan el GIL
    Usar código C/C++ para partes críticas

Por eso, aunque es una limitación real, Python ofrece varias formas de trabajar alrededor de ella según el caso de uso específico.
La clave es entender qué tipo de operaciones estás realizando y elegir la herramienta adecuada:

    I/O intensivo → threads (sincronos) o asyncio(aceptan asincronia)
    CPU intensivo → multiprocessing o bibliotecas optimizadas
    Mixto → combinación de ambos

    RESUMEN: saber como trabajar con concurrencia (sincrona y asincrona) y con paralelismo es clave para elegir como diseñar el codigo
             y lograr mejores resultados 
'''


#EJECUCCION SECUENCIAL - SINCRONA (pueden ser secuencial o concurrente)
'''
    Son bloqueante y se notan si son procesos pesados

    CONCURRENTES (ThreadPoolExecutor):
    Concurrentes en multiples hilos, alternados por el GIL. (Dan la ilusion de paralelismo, pero son concurrentes en multiples hilos)
    No usa event loop, usa callbacks o futures, que se integran al hilo principal de python.

    Pueden ser concurrentes si se usa ThreadPoolExecutor, usando multiples hilos del cpu por ejecucion bloqueante, ya que esta tareas no son async
        with ThreadPoolExecutor(max_workers=3) as executor
    Finalidad es ejecutar funciones síncronas/bloqueantes en hilos separados
    En cada hilo se ejecuta una tarea y con sleep se dice que pasa a otra tarea, haciendo que en realidad
    esto no sea una ejecucion en paralelo, sino ejecucion con pausas en varios hilos, para alterner el permiso de ejecucion o GIL
    El uso de threads en Python no da más capacidad de cómputo por tarea. De hecho, puede ser más lento que la ejecución secuencial para tareas de CPU intensivas debido al overhead de la alternancia del GIL.
    GIL, es como un token que permite la ejecucion de codigo python. Entonces el GIL va rotando entre nucleo.
    Observaciones: 
        Lo que realmente sucede:
        Los threads sí se ejecutan en hilos separados del sistema operativo
        Pero el GIL hace que solo un thread pueda ejecutar código Python a la vez
        El cambio constante entre threads (context switching) añade overhead
        No hay ganancia en capacidad de cómputo, de hecho hay una penalización
    No usar: 
        Para calculos de mucho computo o uso de CPU. Si se quiere mucha capacidad de computo ahi se usa multiprocessing
    Cuando usar:
        Cuando NO PUEDES usar código asíncrono (porque la librería es síncrona):
            import requests  # Librería HTTP síncrona
            from concurrent.futures import ThreadPoolExecutor

            def descargar_archivo(url):
                # requests no soporta async/await
                return requests.get(url)

            def descargar_archivos():
                urls = ['http://api1.com', 'http://api2.com']
                # Necesitas threads porque requests es bloqueante
                with ThreadPoolExecutor() as executor:
                    resultados = executor.map(descargar_archivo, urls)

        Si la libreria soporta asincronismo (la librería soporta async/await) es mejor usar asyncio.gather(*tareas)
    
    Resumen de casos de uso de threands: 
        Los threads se usan cuando:
            Trabajas con librerías antiguas/síncronas
            No puedes modificar el código existente
            Necesitas integrar con sistemas que no son asíncronos
            La librería que necesitas no tiene versión async
        La regla general es:
            Prefiere async/await cuando puedas
            Usa threads cuando debas (código síncrono)
'''

#EJECUCION ASINCRONAS (asincronos o concurrentes)
'''
    No bloquantes
    Ceden el control al event loop y esperan la respuesta en el TaskQueu
    Las peticiones http, pueden ser asincronas o sincronas
    Ocurre en un hilo del nucleo del procesador
    MANEJADO POR EL EVENT LOOP

    CONCURRENTES (cuando se usa gather)
    Pueden ser Concurrentes en caso se envie varias solicitudes asincronas con asyncio.gather(tareas)
    Son concurrentes en un solo hilo,

    tareas = [
        session.get('https://api1.com'),
        session.get('https://api2.com'),
        session.get('https://api3.com')
    ]
    responses = await asyncio.gather(*tareas)
    Finalidad que es agrupar y ejecutar múltiples corrutinas o tareas asíncronas concurrentemente en un solo hilo
'''

#EJECUCION PARALELA 
'''
Para procesos de calculos intensivos de CPU sincronos o asincronos
Python tiene un proceso principal y este su hilo principal, al crear procesos paralelos estamos creando un proceso hijo e hilo principal para este independiente,
donde luego sus resultados se uniran al proceso principal de python
    En Python, cuando inicias un programa:
        El sistema operativo crea el proceso principal
        Dentro de ese proceso, Python crea el hilo principal
        Todo tu código inicial se ejecuta en el hilo principal del proceso principal

        Proceso Principal Python
        └── Hilo Principal del proceso principal
            └── Proceso Hijo
                └── Hilo Principal del proceso hijo
            └── Proceso Hijo
                └── Hilo Principal del proceso hijo
        Cada proceso hijo:
            Tiene su propio PID
            Tiene su propio hilo principal
            Tiene su propio GIL
            Tiene su propia memoria
            Puede crear sus propios hilos adicionales
            Su propia copia de todas las variables
            Su propio intérprete Python
            Sus propios file descriptors
            Su propio event loop (si usa asyncio)
        Por eso el multiprocessing logra verdadero paralelismo: cada proceso hijo es completamente independiente con su propio entorno Python.

Al usar multiprocessing, crea procesos separados
Cada proceso tiene su propio GIL
Mejor para: CPU bound (cálculos intensivos)
Verdadero paralelismo en múltiples cores

    El flujo es:
        El proceso principal Python inicia
        Crea procesos hijos que ejecutan tareas en paralelo
        Los procesos hijos:
            Son independientes
            Tienen su propia memoria
            Ejecutan en diferentes cores
        Los resultados se envían al proceso principal mediante:
        Queues (colas)
        Pipes (tuberías)
        Shared memory (memoria compartida)
        El proceso principal:
            Espera que terminen los hijos (join)
            Recolecta los resultados
            Continúa con su ejecución
        La comunicación entre procesos es más compleja que con threads porque cada proceso tiene su propia memoria aislada.
        Se puede esperar a que todos los hijos terminen y unirlo al proc principal, o tambien
        manejar el resultado independientemente y unirlo cuando acabe cada uno
'''


'''
RESUMEN:
    Si son tareas de calculo intensivo de CPU, ya sean sincronas o asincronas: multiprocessing (ejecucion en paralelo)
    Sin son tareas de solicitues http, descargas de archivos, o que no requieran uso intensivo de CPU y estas soportan asincronismo:
        Asincronos == asyncio(una sola tarea, solo es asincrona) o asyncio.gather(varias tareas - concurrencia un solo hilo)
        Sincronos == Secuancial == Bloqueantes: threading (concurrencia en varios hilos)
'''
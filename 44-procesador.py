#PROCESADOR
'''
El Procesador (CPU):
    Es la unidad principal que contiene todos los núcleos
    Funciona como el "cerebro" completo del computador
    Coordina y distribuye el trabajo entre todos los núcleos disponibles
    Gestiona recursos compartidos como la memoria caché L3 (que usan todos los núcleos)
    Maneja la comunicación con otros componentes del sistema
'''
'''
Relación con los Núcleos:
    Integración física:
        Los núcleos están físicamente integrados dentro del procesador
        Comparten el mismo chip de silicio
        Están conectados por un bus interno de comunicación
    Distribución de tareas:
        El procesador recibe las instrucciones del sistema operativo
        Decide qué núcleo ejecutará cada tarea
        Balancea la carga de trabajo entre los núcleos disponibles (balance de carga porque mientras más computo tiene más carga electrica tiene)
    Gestión de recursos:
        Administra recursos compartidos entre núcleos
        Coordina el acceso a la memoria principal
        Maneja la comunicación entre núcleos cuando necesitan compartir información
'''

#CORE - NUCLEO
'''
Un núcleo físico puede tener típicamente 1 o 2 hilos de procesamiento, aunque esto varía según la tecnología:

Núcleo sin hyperthreading: 1 hilo por núcleo (1 ejecucion por nucleo)
Núcleo con hyperthreading (tecnología de Intel) o SMT (Simultaneous Multi-Threading): 2 hilos por núcleo (3 ejecuciones simultaneas por nucleo, comparten hardware)

La tecnología de hyperthreading/SMT permite que un núcleo físico maneje dos hilos de procesamiento simultáneamente, mejorando la eficiencia cuando se ejecutan múltiples tareas. 
Sin embargo, esto no significa que el rendimiento sea el doble, ya que los hilos (ejecuciones) comparten algunos recursos (hardware) del núcleo.
Es importante mencionar que algunos procesadores más especializados pueden tener más de 2 hilos por núcleo, pero esto es menos común en procesadores de consumo general.
Si tengo 8 nucleos, y cada uno 1 hilo, puedo tener 8 ejecuciones en paralelo
'''
'''
Es el componente físico que realiza las operaciones fundamentales del procesador
Se encarga de ejecutar las instrucciones básicas como cálculos matemáticos y lógicos
Contiene sus propias unidades de control, ALU (Unidad Aritmético-Lógica) y caché
Puede procesar datos de forma independiente de otros núcleos
Es como tener una "mini CPU" completa
'''
'''
La memoria caché está organizada en diferentes niveles, y no toda es compartida:

Caché L1 (Nivel 1):
    Es la más rápida y pequeña
    Cada núcleo tiene su propia caché L1 exclusiva
    Normalmente está dividida en dos partes:
        Caché de instrucciones
        Caché de datos
Caché L2 (Nivel 2):
    Es más grande pero algo más lenta que L1
    Tradicionalmente cada núcleo tiene su propia L2
    Algunos diseños pueden compartirla entre pares de núcleos
Caché L3 (Nivel 3):
    Es la más grande pero la más lenta de las tres
    Esta SÍ es compartida entre todos los núcleos, a nivel de procesador.
    Funciona como último recurso antes de ir a la memoria RAM
    Ayuda en la comunicación entre núcleos

La organización es como una pirámide:
    En la punta está L1 (privada, más rápida, más pequeña)
    En medio L2 (generalmente privada, intermedia)
    En la base L3 (compartida, más grande, más lenta)
Esta estructura permite balancear velocidad y capacidad, mientras mantiene los datos más frecuentemente usados lo más cerca posible de cada núcleo.
'''

#THREAD - HILO
'''
Es una unidad "virtual" de procesamiento (ejecucion, computo)
Se encarga de gestionar una secuencia de instrucciones dentro del núcleo
Permite dividir las tareas en procesos más pequeños que pueden ejecutarse de forma simultánea
Comparte los recursos físicos del núcleo (como la memoria caché y las unidades de procesamiento)
Ayuda a mejorar la eficiencia cuando hay múltiples tareas esperando ser procesadas
'''
'''
Si el núcleo tiene un solo hilo:
    Solo puede ejecutar una tarea a la vez
    Las demás tareas se ponen en una cola de espera
    Tienen que esperar a que termine la tarea actual
    El sistema operativo maneja esta cola y puede hacer "cambios de contexto"

Si el núcleo tiene dos hilos (hyperthreading):
    Puede manejar dos tareas "simultáneamente"
    En realidad alterna muy rápidamente entre ambas tareas
    Comparten los recursos del núcleo
    Si llegan más tareas, estas esperan en cola

El "cambio de contexto" es importante porque:
    Permite pausar momentáneamente una tarea
    Guardar su estado actual
    Ejecutar brevemente otra tarea
    Volver a la primera tarea donde se quedó

    
La gestión de colas ocurre en múltiples niveles:
    A nivel de Procesador:
        Existe una cola principal gestionada por el planificador (scheduler) del sistema operativo
        El planificador decide qué tarea enviar a qué núcleo
        Considera factores como:
            La carga actual de cada núcleo
            La prioridad de las tareas
            La afinidad de proceso (si una tarea tiene preferencia por cierto núcleo)
            El balance de carga entre núcleos
    A nivel de Núcleo:
        Cada núcleo también tiene su propia cola local
        Maneja las tareas que ya le fueron asignadas
        Si un núcleo se sobrecarga, el planificador (scheduler) puede reasignar tareas a otros núcleos
        En caso de hyperthreading, el scheduler gestiona qué tarea dar a cada hilo
'''

#SCHEDULER
'''
El planificador del sistema operativo (scheduler) tiene control tanto a nivel de núcleo como a nivel de hilo. Específicamente:
En procesadores con hyperthreading:
    El planificador ve cada hilo lógico como una unidad de procesamiento independiente
    Puede asignar tareas específicamente a cada hilo dentro del núcleo
    Sabe que los hilos comparten recursos del mismo núcleo físico
    Intenta optimizar qué tipos de tareas ejecutar en paralelo en los hilos del mismo núcleo
    Por ejemplo:
        Si un hilo está ejecutando una tarea intensiva en cálculos
        El planificador podría asignar al otro hilo del mismo núcleo una tarea que usa más operaciones de entrada/salida
        Esto aprovecha mejor los recursos del núcleo ya que ambos tipos de tareas usan diferentes unidades del procesador
El planificador toma estas decisiones miles de veces por segundo, constantemente reajustando y optimizando la distribución de tareas tanto entre núcleos como entre los hilos dentro de cada núcleo.
'''
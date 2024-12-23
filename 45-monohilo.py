#CASO NODEJS - MONO HILO
'''
Vamos a separarlo en capas para entenderlo mejor:
    Nivel Hardware (Tu laptop)
        Tienes 8 núcleos físicos, cada uno con 1 hilo
        Estos son hilos de CPU reales que pueden ejecutar instrucciones en paralelo
        El "sistema operativo" puede asignar procesos y tareas a cualquiera de estos hilos físicos
    Nivel Proceso (Node.js)
        Cuando inicias una aplicación Node.js, creas un proceso (ejecutar una app node es ejecutar una funcion llamada event loop, que gestiona que se ejecutara, 
        en caso sea asincrono lo envia y su futura respuesta estara esperando en el stackqueu, y luego lo devolvera para o bloquear otras ejecuciones sincronas)
        Este proceso puede ser asignado por el sistema operativo a cualquiera de los 8 hilos de CPU disponibles
        El "sistema operativo" puede incluso mover el proceso entre diferentes hilos de CPU según sea necesario
    Nivel Aplicación (El "hilo principal" de Node.js)
        El "hilo principal" no se refiere a un hilo específico de la CPU
        Es un concepto lógico dentro de la aplicación Node.js
        Es donde se ejecuta el Event Loop y tu código JavaScript
        Se le llama "principal" porque es donde se maneja la lógica central de tu aplicación

Aunque este código se ejecuta en el "hilo principal" de Node.js, el proceso completo podría estar corriendo en cualquiera de los 8 hilos de CPU de tu laptop, 
y el sistema operativo podría incluso moverlo entre diferentes hilos de CPU durante su ejecución.
Resaltar que el hilo principal solo es un concepto que se refiere a un gestor de node, que ejecuta el event loop y decide que se ejcutara y lo envia al so y procesador
y como hay ejecuciones async, esta tambien tiene unas micro pilas (stack queu callbacks 2da prioridad, micro stack queue promesas, 1ra prioridad) para las futuras respuestas y no ser bloqueante
'''

'''
El hilo principal de Node.js:
    Ejecuta el Event Loop, que:
        Procesa el código JavaScript
        Maneja la cola de eventos
        Coordina las operaciones asíncronas

    Para operaciones bloqueantes o intensivas:
        Node.js utiliza el thread pool de libuv (por defecto 4 hilos)
        Estas operaciones se ejecutan en paralelo al hilo principal
        El sistema operativo decide en qué núcleo/hilo físico se ejecuta cada cosa

// Esto se ejecuta en el hilo principal
console.log('Inicio');

// Node.js delega esta operación al thread pool de libuv, por requerir mucho computo y ser SINCRONO, demorara y bloquara otras operaciones sincronas por eso crea hilos principlaes en paralelo
fs.readFile('archivo.txt', (err, data) => {
    // El callback vuelve al hilo principal cuando termina
    console.log(data);
});

// Mientras tanto, el hilo principal sigue ejecutando esto
console.log('Fin');

Existen operaciones que se pueden considerar bloqueantes si requieren mucho computa y son sincronas.
Para estos casos NODEJS usa libuv y crea hilos principales paralelos para ejecutar estas multiples tareas bloquantes,
y cuando terminen de resolverse solo se unen al hilo pincipal inicial.

Esas mismas operaciones se deben manejar de forma asincrona para evitar que sean bloqueantes

¿QUE se puede considerar bloqueante?
Que sea algo sincrono y tambien sean
    Operaciones de archivo (fs)
    Operaciones criptográficas
    Operaciones DNS
    Operaciones intensivas de CPU

LIBUV
¿Cómo funciona?
    Cuando llega una operación bloqueante, libuv la asigna a uno de sus hilos del pool
    El hilo principal continúa ejecutando otras tareas
    Cuando el hilo del pool termina, envía el resultado al event loop
    El event loop ejecuta el callback correspondiente
    Las tareas se procesan en paralelo real (no solo concurrencia)
    Aumentar el número de hilos en el pool -> process.env.UV_THREADPOOL_SIZE = 8;

const crypto = require('crypto');
const fs = require('fs');

// Primera operación que usa un hilo del pool
fs.readFile('archivo1.txt', (err, data) => {
    console.log('Archivo 1 leído');
});

// Segunda operación que usa otro hilo del pool
crypto.pbkdf2('pass1', 'salt', 100000, 512, 'sha512', () => {
    console.log('Hash 1 completado');
});

// Tercera operación que usa otro hilo del pool
crypto.pbkdf2('pass2', 'salt', 100000, 512, 'sha512', () => {
    console.log('Hash 2 completado');
});

// Esta operación esperará si el pool está lleno
crypto.pbkdf2('pass3', 'salt', 100000, 512, 'sha512', () => {
    console.log('Hash 3 completado');
});

console.log('Código síncrono ejecutado');

Por defecto: 
libuv viene incluido por defecto en Node.js - es una dependencia central y fundamental. No necesitas instalarlo por separado.
De hecho, libuv es uno de los componentes core de Node.js junto con:
    V8 (el motor JavaScript de Google)
    libuv (para operaciones asíncronas y el event loop)
    c-ares (para resolución DNS)
    llhttp (para parseo HTTP)
Cuando instalas Node.js, todo esto viene empaquetado y listo para usar. Por eso puedes usar funciones asíncronas como fs.readFile() o el módulo http sin ninguna instalación adicional.
Si quieres ver esto en acción, cualquier programa Node.js básico ya está usando libuv por debajo:
'''

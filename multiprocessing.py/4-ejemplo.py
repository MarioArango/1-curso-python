from multiprocessing import Process, Pipe
from time import sleep

'''
Este patrón es útil cuando tienes un flujo de trabajo secuencial donde cada etapa depende de la anterior, como por ejemplo:
Procesamiento de imágenes (cargar → aplicar filtros → guardar)
ETL de datos (extraer → transformar → cargar)
Procesamiento de audio (leer → aplicar efectos → exportar)
'''

def lector(conn_out):
    '''Primera etapa: Lee datos (simula leer de un archivo)'''
    textos = [
        'hola mundo',
        'python es genial',
        'programacion multriprocess'
    ]

    for texto in textos:
        print(f'Leyendo: {texto}')
        conn_out.send(texto)
        sleep(1) #simulamos un tiempo de lectura

    #Envia señal de terminacion
    conn_out.send(None)
    conn_out.close()

def transformador(conn_in, conn_out):
    '''Segunda etapa: Transforma los datos en mayuscula'''
    while True:
        texto = conn_in.recv() #Recive texto de la etapa anterior

        if texto is None:
            break
            
        text_transformado = texto.upper()
        print(f'Transformado: {texto} -> {text_transformado}')
        conn_out.send(text_transformado)

    #propaga la señal de terminacion
    conn_out.send(None)
    conn_out.close()

def escritor(conn_in):
    '''Tercera etapa: Escribe los resultados'''
    while True:
        texto = conn_in.recv() #recibe el texto transformado

        if texto is None:
            break

        print(f'Guardando resultado: {texto}')

if __name__ == '__main__':
    #crear las conexiones entre procesos
    pipe1_in, pipe1_out = Pipe() #conecta lector -> transformador
    pipe2_in, pipe2_out = Pipe() #conecta transformador -> escritor

    #crear procesos
    p1 = Process(target=lector, args=(pipe1_out,))
    p2 = Process(target=transformador, args=(pipe1_in, pipe2_out))
    p3 = Process(target=escritor, args=(pipe2_in,))

    #Iniciar los procesos
    print('Iniciando...')
    p1.start()
    p2.start()
    p3.start()

    #Esperar a que terminen los procesos
    p1.join()
    p2.join()
    p3.join()
    print('Proceses completados')
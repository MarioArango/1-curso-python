import asyncio
import time

async def download_file(name, time):
    print(f'Iniciando descarga de {name}')
    await asyncio.sleep(time) #simula tiempo de descarga
    print(f'Completa descarga de {name}')
    return f'{name} descargado'

async def main():
    inicio = time.time()

    #ejecucion secuencial de tareas
    #el código se ejecuta de forma secuencial y bloqueante. 
    resultado1 = await download_file('archivo1.txt', 2)
    resultado2 = await download_file('archivo2.txt', 3)
    resultado3 = await download_file('archivo3.txt', 1)

    fin = time.time()
    print(f'Tiempo total: {fin - inicio:.2f} segundos')
    print(f'Resultados: {resultado1}, {resultado2}, {resultado3}')

async def main_concurrente():
    inicio = time.time()

    # Ejecución paralela
    resultados = await asyncio.gather(
        download_file("archivo1.txt", 2),  # Comienza inmediatamente
        download_file("archivo2.txt", 3),  # Comienza inmediatamente
        download_file("archivo3.txt", 1)   # Comienza inmediatamente
    )

    fin = time.time()
    print(f'Tiempo total: {fin - inicio:.2f} segundos')
    print(f'Resultados: {resultados}')

asyncio.run(main()) #asincronia bloquante en cada await
asyncio.run(main_concurrente()) #asincronia concurrente en el mismo hilo
import asyncio
import time

async def descargar_archivo(nombre, tiempo):
    print(f"Iniciando descarga de {nombre}")
    await asyncio.sleep(tiempo)  # Simula tiempo de descarga
    print(f"Completada descarga de {nombre}")
    return f"{nombre} descargado"

async def main():
    inicio = time.time()
    
    # Ejecución paralela usando gather
    resultados = await asyncio.gather(
        descargar_archivo("archivo1.txt", 2),
        descargar_archivo("archivo2.txt", 3),
        descargar_archivo("archivo3.txt", 1)
    )
    
    fin = time.time()
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print(f"Resultados: {resultados}")

asyncio.run(main())
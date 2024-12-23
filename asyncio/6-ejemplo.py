import asyncio
import random

async def monitorear_servicio(nombre, intervalo):
    for _ in range(3):
        await asyncio.sleep(intervalo)
        estado = random.choice(['activo', 'inactivo'])
        print(f"Servicio {nombre}: {estado}")
        if estado == 'inactivo':
            raise Exception(f"¡Servicio {nombre} caído!")
        return f"Servicio {nombre} OK"

async def main():
    servicios = [
        monitorear_servicio("Base de datos", 1),
        monitorear_servicio("API", 2),
        monitorear_servicio("Cache", 1.5)
    ]
    
    resultados = await asyncio.gather(*servicios, return_exceptions=True)
    
    for nombre, resultado in zip(['Base de datos', 'API', 'Cache'], resultados):
        if isinstance(resultado, Exception):
            print(f"{nombre}: {resultado}")
        else:
            print(f"{nombre}: {resultado}")

asyncio.run(main())
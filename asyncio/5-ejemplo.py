import asyncio

async def procesar_dato(id_dato):
    await asyncio.sleep(1)
    if id_dato % 2 == 0:
        return f"Dato {id_dato} procesado"
    else:
        raise ValueError(f"Error en dato {id_dato}")

async def main():
    # Procesamiento paralelo con manejo de errores
    resultados = await asyncio.gather(
        procesar_dato(1),
        procesar_dato(2),
        procesar_dato(3),
        return_exceptions=True  # Importante: permite continuar aunque haya errores
    )
    
    for resultado in resultados:
        if isinstance(resultado, Exception):
            print(f"Error: {resultado}")
        else:
            print(f"Éxito: {resultado}")

asyncio.run(main())
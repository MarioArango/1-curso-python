import asyncio

async def procesar_evento(id_evento):
    print(f"Procesando evento {id_evento}")
    await asyncio.sleep(1)
    if id_evento % 2 == 0:
        return f"Evento {id_evento} procesado con éxito"
    else:
        raise Exception(f"Error en evento {id_evento}")

async def main():
    try:
        resultado = await procesar_evento(1)
        print(resultado)
    except Exception as e:
        print(f"Error capturado: {e}")
    
    try:
        resultado = await procesar_evento(2)
        print(resultado)
    except Exception as e:
        print(f"Error capturado: {e}")

asyncio.run(main())
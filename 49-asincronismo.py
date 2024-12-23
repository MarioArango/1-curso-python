import asyncio

async def process_data(data):
    print(f'Procesando {data}...')
    #Simular una operacion, suspende y espera, si fuere time lo bloquearia
    await asyncio.sleep(10)
    print(f'{data} procesado.')
    return data*2

#funcion principal donde se ejecutan las corrutinas
async def main():
    print(f'Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

#Iniciamos el event loop
asyncio.run(main())
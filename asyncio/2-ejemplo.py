import asyncio

async def tarea_prioritaria():
    for i in range(3):
        print(f'Tarea prioritaria: {i}')
        await asyncio.sleep(1)

async def tarea_secundaria():
    for i in range(5):
        print(f'Tarea secundaria: {i}')
        await asyncio.sleep(2)

async def main():
    #Crear las tareas
    await asyncio.create_task(tarea_prioritaria())
    await asyncio.create_task(tarea_secundaria())


asyncio.run(main()) #asincronia bloqueante en cada await
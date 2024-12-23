import asyncio
import time
import random
import multiprocessing

'''
Node.js: "Don't make the developer think about it", nodej lo maneja en automatico o implicita con libuv
Python: "Explicit is better than implicit", tenemos la posibilidad de manjearlo de forma explicita
'''

#Funcion asincrona para verificar el inventario
async def check_inventory(item):
    print(f'Verificando inventario para {item}...')
    await asyncio.sleep(random.randint(3, 6))
    print(f'Inventario verificado para {item}')
    #Similar disponibilidad del producto
    return random.choice([True, False])

#Funcion asincrona para procesar el pago
async def process_payment(order_id):
    print(f'Procesando pago para la orden {order_id}...')
    #Simula el tiempo de espera para procesar el pago
    await asyncio.sleep(random.randint(3, 6))
    print(f'Pago procesado para la orden {order_id}')
    return True

#Funcion intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    print(f'Calculando el costo total para {len(items)} articulos...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'Costo total calculado: ${total}')
    return total

#Funcion asincrona para procesar la orden
async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden {order_id}...')
    #Verifica inventario para cada articulo
    inventory_check = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_check)

    if not all(inventory_results): #all: retorna True si todos son True
        print(f'Orden {order_id} cancelado: Producto no disponible')
    
    with multiprocessing.Pool() as pool: #usara todos los nucleos disponibles
        total = pool.apply(calculate_total, args=(items,)) #apply_async
        # total_result = total.get()

    #Procesar el pago asincronamente
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Orden {order_id} completado con exito!, Total: ${total}')
    else:
        print(f'Orden {order_id} fallo: Error al procesar el pago')

async def main():
    orders = [
        {
            'order_id': 1,
            'items': [
                {
                    'name': 'Laptop',
                    'price': 1000
                },
                {
                    'name': 'Mouse',
                    'price': 20
                }
            ]
        },
        {
            'order_id': 2,
            'items': [
                {
                    'name': 'Monitor',
                    'price': 300
                },
                {
                    'name': 'Teclado',
                    'price': 50
                }
            ]
        },
        {
            'order_id': 3,
            'items': [
                {
                    'name': 'Headphones',
                    'price': 70
                },
                {
                    'name': 'Webcam',
                    'price': 50
                }
            ]
        }
    ]

    #procesamos las multiples ordenes concurrentemente
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

#Creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())
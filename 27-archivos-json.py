import json

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

# with open('./products.json', mode='r') as file:
#     products = json.load(file) #lista de diccionarios
#     for product in products:
#             print(product)

with open('./products.json', mode='r') as file:
    products = json.load(file) #lista de diccionarios
    products.append(new_product)
    with open('./products_updated.json', mode='w') as file_updated:
        json.dump(products, file_updated, indent=4)
import csv

# #Leer un archivo y transformarlo en formato diccionario
with open('./products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['price'])

product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

# #Escribe una nueva linea al final, newline hace que el salto de linea sea automatico
with open('./products.csv', 'a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames = product.keys())
    csv_writer.writerow(product)

#Como buena practica no es recomendable editar el archivo fuente, es mejor crear una copia
# 1.extraemos el archivo fuente mode='r' para leer
# 2.creamos el archivo de trabajo mode'w' para escribir
# 3.copiamos cabeceras y registros, para copiar y pegar
#Para lograrlo debemos trabajar con una lista de diccionarios, que nos provee el cast el import csv

#1
with open('./products.csv', mode='r') as source_file:
    list_dict_source_file = csv.DictReader(source_file)
    #2
    with open('./products_to_work.csv', mode='w', newline='') as work_file:
        #3
        fieldnames = list_dict_source_file.fieldnames + ['total_value']
        list_dict_work_file = csv.DictWriter(work_file, fieldnames)
        list_dict_work_file.writeheader()
        for row in list_dict_source_file:
            row['total_value'] = float(row['price'])*int(row['quantity'])
            list_dict_work_file.writerow(row)


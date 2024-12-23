import statistics
import csv

#Leer los datos de ventas mensuales desde un csv
sales_by_moth = {}
with open('./statistics_data.csv', mode='r') as file:
    list_sales = csv.DictReader(file)
    for sale in list_sales:
        month = sale['month']
        sale = float(sale['sales'])
        sales_by_moth[month] = sale
    
    sales = list(sales_by_moth.values())
    
    #El valor que representa todo el conjunto
    mean_sales = statistics.mean(sales)
    print(f'El promedio es: {mean_sales}')

    #Valor medio entre el min y max
    median_sales = statistics.median(sales)
    print(f'La mediana es: {median_sales}')

    #Que valor se repite más
    mode_sales = statistics.mode(sales)
    print(f'La moda es: {mode_sales}')

    stdev_sales = statistics.stdev(sales)
    print(f'La desviacion estandar es: {stdev_sales}')

    variance_sales = statistics.variance(sales)
    print(f'La varianza es: {variance_sales}')

    min_sales = min(sales)
    max_sales = max(sales)
    print(f'El minimo valor es {min_sales} y el maximo es {max_sales}')
    range_sales = max_sales - min_sales
    print(f'El Rango de ventas es: {range_sales}')
#Trae todo el archivo
# with open('./texto.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

#Trae todo el archivo linea por linea
# with open('./texto.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.strip()) #quita el salto de linea  

# Trae en una lista cada linea del texto
with open('./texto.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(len(lines))

#Agrega texto al final mode='a' append
# with open('./texto.txt', 'a', encoding='utf-8') as file:
#     file.write('\nNueva linea agrgada\n')

# #Reemplaza todo el contenido y si el archivo no existe lo cre
# with open('./texto.txt', 'w', encoding='utf-8') as file:
#     file.write('Nuevo texto')

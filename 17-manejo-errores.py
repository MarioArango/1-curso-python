# try:
#     number = int(input('Ingrese un numero: '))
#     division = 100/number
#     print(division)
# except ZeroDivisionError as error:
#     print('hubo un error del tipo:', error)
# except ValueError as error:
#     print('Debe ingresar un número, no un caracter: ', error)
# except NameError as error:
#     print('Error general', error)
# except: #Exception as error:
#     print('Hubo un error general')

# def verificar_edad(edad):
#     try:
#         if edad < 0:
#             raise ValueError("La edad no puede ser negativa")
#         elif edad < 18:
#             raise Exception("La persona es menor de edad")
#         else:
#             return "Edad válida"
#     except:
#         return 'Error'


# print(verificar_edad(-1))

#Jerarquia de Exception
def print_exception_hierarchy(exception_class, indent = 0):
    print('' * indent + exception_class.__name__ )
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)
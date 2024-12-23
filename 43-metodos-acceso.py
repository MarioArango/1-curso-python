class Padre:
    def __init__(self, name, phone, dni):
        self.name = name
        self._phone = phone
        self.__dni = dni
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    #Tambien python reconoce los metodos privados con 2guion bajo de inicio
    def __metodo_privador_del_padre(self):
        print('Hola')

    def saludar(self):
        self.__metodo_privador_del_padre()

mario = Padre('Mario', '924747374', '72935585')
print(mario.name) #publico
print(mario._phone) #publico, pero cuando los devs lo vean con 1 guion, entenderan que no se puede editar directamente, sino mediante un setter
# print(mario.__dni) #privado, python no lo mostrara, dara error
print(mario.dni) #se puede acceder mediante un getter y editar con un setter
mario.dni = 123
print(mario.dni)
mario.saludar()

print('--------------------')

class Hijo(Padre):
    def __init__(self, name, phone, dni, name_child):
        super().__init__(name, phone, dni)
        self.__name_child = name_child

    @property
    def name_child(self):
        return self.__name_child

    @name_child.setter
    def name_child(self, name):
        self.__name_child = name

    @name_child.deleter #permite eliminar la propiedad
    def name_child(self):
        del self.__name_child

debbi = Hijo('Mario', '924747374', '72935585', 'Debbi')
print(f'Nombre del padre: {debbi.name}')
print(f'Telefono del padre: {debbi._phone}')
print(f'Dni del padre: {debbi.dni}') #se puede acceder porque es un getter
print(f'Nombre del hijo: {debbi.name_child}')
del debbi.name_child #eliminar la propiedad
print(f'Nombre eliminado: {getattr(debbi, 'name_child', 'No existe')}')
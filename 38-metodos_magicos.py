#METODOS MAGICOS O METODOS DUNDER
#Sobrecarga de operadores
#Solo usar cuando tenga sentido
#Mantener la consistenia
#Documentar el comportamiento

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    #metodo magico que devuelve una presentacion amigable de los atributos de la clase, como string: str
    def __str__(self) -> str:
        #Nombre de la clase: attr1, attrb2, ...
        return f'Persona: {self.nombre}, {self.edad} años'
    
    def __repr__(self) -> str:
        #Devuelve una representacion detallada del objeto para depuracion
        #Es una representacion de como se instancia la clase, asi sabemos que atributos tiene
        return f"Persona(nombre='{self.nombre}', edad: '{self.edad}')"
    
    #Como comparar la instancia al usar la igualdad
    #comparamos primitivos 1 == 1, comparamos lista [1,2] == [1,2] elemento por elemento
    #si queremos crear como se debe comparar mi clase, se define mediante que comparar
    def __eq__(self, other_self) -> bool:
        return self.nombre == other_self.nombre and self.edad == other_self.edad
    
    def __lt__(self, other_self) -> bool:
        return self.edad < other_self.edad
    
    #Crea una nueva instancia sumando las edades
    def __add__(self, other_self):
        return Persona(self.nombre, self.edad + other_self.edad)

mario = Persona('Mario', 29)
mario2 = Persona('Mario', 29)

#Como personalizamos el metodo magico __str__, al imprimir la instancia ya no devolvera la ref memoria, sino algo legible
print(mario)

#Como personalizamos el metodo magico __repr__, al imprimir la instancia con repr ya no devolvera la ref memoria, sino algo legible
#Como instanciar
print(repr(mario))

#Como personalizamos __eq__, definimos cuando se consideran igual en mis instancias
print(mario == mario2)

#Como personalizamos __lt__, definimos que instancia se considera mayor
print(mario > mario2)

#Como personalizamos __add__, definimos como es la suma de instancias
print(mario + mario2)
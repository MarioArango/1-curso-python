class Calculator:
    
    #Se usa si no accedemos ni modificamos atributos de la clase
    #Es una función que podría existir perfectamente fuera de la clase.
    #Mantener esta función dentro de la clase por organización lógica
    #Llamarla directamente desde la clase sin crear una instancia
    #Evitar el parámetro self ya que no lo necesitamos, ya que una clase necesitan self como primer parámetro porque necesitan acceder a los atributos o métodos de la instancia de la clase
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def es_email_valido(email: str) -> bool:
        # Simple validación que verifica @ y .
        return '@' in email and '.' in email
    
    @staticmethod
    def es_numero_positivo(numero: float) -> bool:
        return numero > 0
    
#Son metodos que pueden exister fuera de la clase, pero por cuestiones de orden y agrupamiento de logica van dentro
#por lo que pueden ser accedidos sin previa instancia
# print(Calculator.add(1, 2))
# print(Calculator.es_email_valido('mario@gmail.com'))
# print(Calculator.es_numero_positivo(0))

class Counter:
    count = 0 #atributo de clase, porque es cte y no sera parte de un parametro del metodo constructor

    def __init__(self, name):
        self.name = name

    @staticmethod #metodo de clase, porque no usa atributos
    def saludar():
        return 'hola'

    #Se usa para manejar atributos o metodos de clase, es decir constantes o metodos estaticmethods
    #Se usa para manejar diferentes formatos de entrada, es decir que permita instanciar de varias formas
    #Juegan con datos globales para la clase y por ende para todas las instancias
    #RESUMEN: es un metodo estatico que utiliza algun atributo o metodo de clase "cls"
    @classmethod
    def increment(cls):
        cls.count += 1 #editando el atributo de clase
    
    #Tambien se usa para crear constructores alternativos
    @classmethod
    def constructor_alternativo(cls, name):
        return cls(name)

Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.count)
counterCustom = Counter.constructor_alternativo('Mario')
print(counterCustom.count)

#Esta nueva instancia ya recibe el atributo de clase editado
counter = Counter('jesus')
print(counter.count)

class Persona:
    def __init__(self, name, lastname):
        #Una convencion es usar guin abajo al empezar para propiedades privadas
        #y más abajo establecer getters y setters con el decorador @property
        self._name = name
        self._lastname = lastname
    
    #GETTER DE _name
    #Se usa para crear getter y setters
    #No puede existir setter sin getter
    @property
    def name(self):
        return self._name
    
    #nombre_del_decorador_getter.setter
    @name.setter
    def name(self, name):
        self._name = name

mario = Persona('Mario', 'Arango')
print(mario.name)
mario.name = 'Jesus'
print(mario.name)

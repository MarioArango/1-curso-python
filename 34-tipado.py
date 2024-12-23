from typing import Optional, Union
# Las anotaciones de tipo en Python (como id1: int) son solo sugerencias
# y no se verifican en tiempo de ejecución como lo haria typescript, porque
# python es dinamico y ts es statico
# debido a ello se usa la libreria standar mypy para validar los tipos
# id1: int = '1'
# id2 = 2
# id3: str = id1 + id2

#Optional es la forma sugar de escribir Union
#La diferenia es que Optional acepta dos valores y union puede aceptar más

class Employee:
    def __init__(self, name: str, age: int, salary: float, is_active: bool):
        self.name = name
        self.age = age
        self.salary = salary
        self.is_active = is_active
    
    def get_name(self) -> Optional[str]:
        #Optional le dice que puede retornar el tipo o None 
        value = self.name if self.name else None
        return value
    
    #el parametro puede ser un bool o none
    def get_salary(self, is_active: Union[bool, int, float, list, dict, tuple, None]) -> float:
        value = self.salary if hasattr(self, 'name') else getattr(self, 'name', 'name por defecto')
        return value

employee = Employee('Mario', 29, 3500, True)
employee.get_name()

def divide(a: int, b: int) -> float:
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Error: ambos parametros enteros o flotantes')
        if b == 0:
            raise ValueError('Error: El divisor no puede ser cero')
        return a/b
    except (ValueError, TypeError) as e:
        print(f'Hubo un error: {e}')

divide(10,1)
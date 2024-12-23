#1. Marcar un directorio como Paquete Python:

#2. Inicializar variables/importaciones del paquete:
# from .modulo1 import FuncionA
# from .modulo2 import FuncionB
VERSION = '1.0.0'
AUTOR = 'Juan Perez'

#3. Controlar qué se expone con __all__:
'''
from .modulo1 import FuncionA, FuncionB
from .modulo2 import ClaseX

__all__ = ['FuncionA', 'ClaseX']
'''

#4. Ejecutar código de inicialización:
print("Inicializando el paquete...")

#5. Simplificar importaciones:
'''
# Sin __init__.py
from mi_paquete.modulo1.submodulo import funcion

# Con __init__.py (si defines las importaciones ahí)
from mi_paquete import funcion

'''
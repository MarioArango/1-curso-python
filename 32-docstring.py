import math

def calculate_area_square(width):
    '''
        Calcula el area de un cuadrado
        Parametros:
            width: lado del cuadrado
        Retorna: 
            El area de cuadrado
    '''
    return width**2

def calculate_area_circle(radius):
    '''
        Calcula el area del circulo
        Parametros:
            radius: medida del radio en metros
        Retorna:
            El area de circulo
    '''

    #Constante amtematica pi
    PI = math.pi

    return PI*(radius**2)
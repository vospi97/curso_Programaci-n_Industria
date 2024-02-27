# Funciones

def suma(num1: float, num2: float) -> float: # La flecha me indica qué tipo de dato me retorna
     
    """Suma dos flotantes

    Args:
        num1(float)
        num2(float)

    Return:
        float: resultado de la suma de los dos números anteriores

    """
    valor_suma: float = num1 + num2
    return valor_suma

# Ejercicio: escribir una función que muestra por pantalla "Hola Mundo"

def hola_mundo() -> None:
    print('Hola Mundo')

def saludo (nombre:str) -> None:
    saludo = f"Hola {nombre}"
    print(saludo)

saludo('Mirrey')

# Escribir una función que reciba un núemero entero y devuelva su factorial

import math
def factorial(numero: int) -> int:
    """Esta función calcula el factorial de un entero

    Args:
        numero (int): número al cual le saco el factorial

    Returns:
        int: valor del factorial
    """
    
    factorial = math.factorial(numero)
    return factorial

print(factorial(5))

# Escribir una función que reciba una lista de números y retorne su media 
import numpy as np
def media(lista: list) -> float:
    """Esta función recibe una lista de números y me devuelve su media

    Args:
        lista (list): lista de números

    Returns:
        float: _promedio de los números en la lista
    """
    
    return sum(lista) / len(lista)


lista1 = [3,4,5,2,8]
print(media(lista1))
"""
Funciones de la calculadora.
"""

AUTOR = "jeronimo, Esteban, Carlos, Mauricio"


def sumar(a, b):
    """
    funcion que recibe 2 numero y los suma.
    """
    return a + b


def restar(a, b):
    """
    funcion que recibe 2 numero y los resta.
    """
    return a - b


def multiplicar(a, b):
    """
    funcion que recibe 2 numero y los multiplica.
    """
    return a * b


def dividir(a, b):
    """
    funcion que recibe 2 numero y los divide.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """
    funcion que recibe 2 numero y los eleva a la potencia.
    """
    return a**b


def modulo(a, b):
    """
    funcion que recibe 2 numero y devuelve el resto de la division.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a % b

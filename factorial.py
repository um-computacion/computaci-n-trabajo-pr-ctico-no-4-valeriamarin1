def factorial_iterative(n):
    """
    Calcula el factorial de un número de forma iterativa.
    """
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calcula el factorial de un número de forma recursiva.
    """
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


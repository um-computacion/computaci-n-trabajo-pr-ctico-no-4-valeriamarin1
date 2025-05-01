def fibonacci_iterative(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma iterativa.

    Parámetros:
        n (int): Posición en la secuencia (n ≥ 1).

    Devuelve:
        int: El valor de Fibonacci en la posición n.

    Lanza:
        ValueError: Si n < 1.
    """
    if n < 1:
        raise ValueError("n debe ser mayor o igual a 1.")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma recursiva.

    Parámetros:
        n (int): Posición en la secuencia (n ≥ 1).

    Devuelve:
        int: El valor de Fibonacci en la posición n.

    Lanza:
        ValueError: Si n < 1.
    """
    if n < 1:
        raise ValueError("n debe ser mayor o igual a 1.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

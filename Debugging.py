def f(x, y):
    """
    >>> f(1, 2)
    -1
    >>> f(2, 3)
    -1
    """
    return x-y

def factLoop(n):
    """
        >>> factLoop(3)
        6
    """

    total = 1
    for i in range(n):
        total*=i
    return total





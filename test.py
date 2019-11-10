def prime_factors(x):
    """
    12 -> 1, 2, 2, 3
    17 -> 1, 17

    Function description.
    :type x: int,>=1
    :rtype: dict[>0](int:(int,>=1))

    >>> prime_factors(1)
    {1: 1}
    >>> prime_factors(2)
    {1: 1, 2: 1}
    >>> prime_factors(3)
    {1: 1, 3: 1}
    >>> prime_factors(4)
    {1: 1, 2: 2}
    >>> prime_factors(10)
    {1: 1, 2: 1, 5: 1}
    >>> prime_factors(12)
    {1: 1, 2: 2, 3: 1}
    >>> prime_factors(17)
    {1: 1, 17: 1}
    >>> prime_factors(1024)
    {1: 1, 2: 10}

    """
    factors = {1: 1}
    i = 2
    while i <= x ** 0.5:
        if x % i != 0:
            i += 1
        else:
            factors[i] = factors.get(i, 0) + 1
            x //= i
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors

if __name__ == "__main__":
    import doctest
    doctest.testmod()

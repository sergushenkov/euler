from contracts import contract


@contract
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


@contract
def smallest_multiply(factors1, factors2):
    """
    (1, 2, 2, 3) + (1, 2, 5) -> (1, 2, 2, 3, 5)
    for 12 and 10 smallest multiply is 60

    Function description.
    :type factors1: dict[>0](int:(int,>=1))
    :type factors2: dict[>0](int:(int,>=1))
    :rtype: dict[>0](int:(int,>=1))

    >>> smallest_multiply(prime_factors(1), prime_factors(12))
    {1: 1, 2: 2, 3: 1}
    >>> smallest_multiply(prime_factors(17), prime_factors(19))
    {1: 1, 17: 1, 19: 1}
    >>> smallest_multiply(prime_factors(12), prime_factors(120))
    {1: 1, 2: 3, 3: 1, 5: 1}

    """
    for factor, reps in factors2.items():
        if factor not in factors1:
            factors1[factor] = reps
        elif reps > factors1[factor]:
            factors1[factor] = reps
    return factors1


@contract
def factors(x):
    """
    12 -> 1, 2, 2, 3
    17 -> 1, 17

    Function description.
    :type x: int,>=1
    :rtype: set[>0](int, >0)

    >>> factors(1)
    {1}
    >>> factors(2)
    {1, 2}
    >>> factors(3)
    {1, 3}
    >>> factors(4)
    {1, 2, 4}
    >>> factors(10)
    {1, 10, 2, 5}
    >>> factors(12)
    {1, 2, 3, 4, 6, 12}
    >>> factors(17)
    {1, 17}
    >>> factors(1024)
    {1024, 1, 2, 512, 4, 256, 128, 64, 8, 32, 16}

    """
    factors = {1, x}
    i = 2
    while i <= x // i:
        if x % i != 0:
            i += 1
        else:
            factors.add(i)
            factors.add(x//i)
            i += 1
    return factors


@contract
def collatz(x):
    """
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (len = 10)
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Function description.
    :type x: int,>=1
    :rtype: int, >=1
    
    >>> collatz(1)
    1
    >>> collatz(13)
    10
    """
    count = 1
    while x != 1:
        if x%2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        count += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

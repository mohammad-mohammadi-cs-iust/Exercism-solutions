def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = set()
    for x in range(1,number//2 +1):
        if x in factors:
            break
        if number % x == 0:
            factors.add(x)
    summ = sum(factors)
    if summ == number:
        return 'perfect'
    elif summ > number:
        return 'abundant'
    else:
        return 'deficient'
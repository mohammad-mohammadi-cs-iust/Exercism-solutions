def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    summ = sum(x for x in range(1, number // 2 + 1) if number % x == 0)
    if summ == number:
        return 'perfect'
    elif summ > number:
        return 'abundant'
    else:
        return 'deficient'
        
        

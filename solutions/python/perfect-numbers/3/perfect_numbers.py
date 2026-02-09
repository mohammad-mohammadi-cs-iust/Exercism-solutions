import math

def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors_sum = 0

    for x in range(1, int(math.sqrt(number)) + 1):
        if number % x == 0:
            pair = number // x

            if x != number:
                factors_sum += x
            if pair != x and pair != number:
                factors_sum += pair

    if factors_sum == number:
        return 'perfect'
    elif factors_sum > number:
        return 'abundant'
    else:
        return 'deficient'
        
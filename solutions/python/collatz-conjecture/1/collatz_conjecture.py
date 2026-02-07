def steps(number):
    step = 0
    while number > 1:
        if number % 2 == 0:
            number //= 2
            step += 1
        else:
            number = number*3 + 1
            step += 1
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        return
    return step
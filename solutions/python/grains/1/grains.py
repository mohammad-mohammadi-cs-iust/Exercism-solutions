def square(number):
    if 1<=number<=64:
        return 2**(number - 1)
    else:
        raise ValueError("square must be between 1 and 64")
        return


def total():
    return sum(square(x) for x in range(1,65))

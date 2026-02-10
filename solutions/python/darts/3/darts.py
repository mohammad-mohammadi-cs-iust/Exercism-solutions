def score(x, y):
    summ = x**2 + y**2
    if summ <= 1:
        return 10
    if summ <= 25:
        return 5
    if summ <= 100:
        return 1
    
    return 0

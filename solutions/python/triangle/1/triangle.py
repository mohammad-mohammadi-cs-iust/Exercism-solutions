def equilateral(sides):
    for i in range(len(sides)):
        if sides[i] > sum(sides) - sides[i]:
            return False
    if 0 in sides:
        return False
    if len(set(sides)) == 1:
        return True
    return False


def isosceles(sides):
    for i in range(len(sides)):
        if sides[i] > sum(sides) - sides[i]:
            return False
    if 0 in sides:
        return False
    if len(set(sides)) < 3:
        return True
    return False
    



def scalene(sides):
    for i in range(len(sides)):
        if sides[i] > sum(sides) - sides[i]:
            return False
    if 0 in sides:
        return False
    if len(set(sides)) == 3:
        return True
    return False
    


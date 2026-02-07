def is_armstrong_number(number):
    if number == sum(int(ch)**len(str(number)) for ch in str(number)):
        return True
    return False

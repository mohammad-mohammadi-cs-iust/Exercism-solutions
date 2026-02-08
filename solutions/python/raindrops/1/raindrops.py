def convert(number):
    sound = ""
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    if number % 3 and number % 5 and number % 7:
        return str(number)
    else:
        return sound

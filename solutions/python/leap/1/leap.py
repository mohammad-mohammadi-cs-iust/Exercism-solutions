def leap_year(year):
    if year % 4:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 3:
        return False
    elif year % 100 == 0 and year % 400:
        return False
    elif year % 200 == 0 and year % 400:
        return False
    else:
        return True
    
        
    

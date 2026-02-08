def is_armstrong_number(number):
    num_of_digits = 0
    for ch in str(number):
        num_of_digits += 1
    
    return number == sum(int(ch)**num_of_digits for ch in str(number))
        

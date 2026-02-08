def is_armstrong_number(number):
    str_num = str(number)
    power = len(str_num)
    return number == sum(int(ch)**power for ch in str_num)
        

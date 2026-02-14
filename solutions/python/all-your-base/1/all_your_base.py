def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for d in digits:
        if not (0 <= d < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    decimal = rebase_to_ten(input_base,digits)
    return final_rebase(decimal,output_base)       
def rebase_to_ten(input_base, digits,):
    '''this function takes the character and its index by enumerating;
      >>then takes the place value of the integer-line9-(len(digits) - idx - 1);
      >>then takes the base into power of the pv;
      >>finally multiplies it to the integer char;
      >>decimal number is ready!
      '''
    decimal = 0
    for idx , d in enumerate(digits):
        decimal += d * (input_base ** (len(digits) - idx - 1))
    return decimal
def final_rebase(decimal,output_base):
    '''this function algorithm is based on division algorithm (a = bq + r, 0 <= r < |b|);
    >>taking the remainder of initial divison;
    >>adding it to the string of final_base number;
    >>replacing the quotient as dividend;
    >>repeating process till dividend < divisor;
    
    '''
    if decimal == 0:
        return [0]
    final_result = []
    while  decimal > 0:
        final_result.append( decimal % output_base)
        decimal //= output_base
    return final_result[::-1]
    
    
    
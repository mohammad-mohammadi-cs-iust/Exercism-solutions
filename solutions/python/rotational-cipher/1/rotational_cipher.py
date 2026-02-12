def rotate(text, key):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for ch in text:
        if ch in lowers:
            idx = lowers.index(ch)
            ch1 = lowers[(idx + key) % 26]
            result += ch1
        elif ch in uppers:
            idx = uppers.index(ch)
            ch1 = uppers[(idx + key) % 26]
            result += ch1
        else:
            result += ch
    return result
        

def is_isogram(string):
    s = [ch.lower() for ch in string if ch.isalpha()]
    return len(s) == len(set(s))
    

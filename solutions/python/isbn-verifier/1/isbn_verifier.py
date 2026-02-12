def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    
    return sum((10 if ch == 'X' else int(ch)) * (10 - i) for i, ch in enumerate(isbn) ) % 11 == 0

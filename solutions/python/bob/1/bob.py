def response(hey_bob):
    hey_bob_clean = hey_bob.strip()
    if hey_bob_clean != "" and hey_bob[-1] == '?' and hey_bob.upper() == hey_bob and tuple(x for x in hey_bob if x in 'ABCDDEFGHIJKLMNOPQRSTUVWXYZ'):
        return "Calm down, I know what I'm doing!"
    elif hey_bob_clean != "" and hey_bob_clean[-1] == '?':
        return "Sure."
    elif hey_bob.upper() == hey_bob and tuple(x for x in hey_bob if x in 'ABCDDEFGHIJKLMNOPQRSTUVWXYZ'):
        return "Whoa, chill out!"
    elif hey_bob_clean == "" :
        return "Fine. Be that way!"
    return "Whatever." 

    

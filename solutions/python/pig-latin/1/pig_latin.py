def translate(phrase):
    phrasee = []
    for text in phrase.split():    
        if text[0] in "aeiou":
            final_text = text + "ay"
        elif text[:2] == "xr" or text[:2] == "yt":
            final_text = text + "ay"
        else:
            for i in range(len(text)):
                if text[i] in "aeiuo":
                    final_text = text[i:] + text[:i] + "ay"
                    break
                elif text[i] == "q" and text[i + 1] == "u":
                    final_text = text[i+2:] + text[:i+2] + "ay"
                    break
                elif text[i] == "y" and text[(i + 1) % len(text)] not in "aeiou":
                    final_text = text[i:] + text[:i] + "ay"
                    break
        phrasee.append(final_text)
    return " ".join(phrasee)


        


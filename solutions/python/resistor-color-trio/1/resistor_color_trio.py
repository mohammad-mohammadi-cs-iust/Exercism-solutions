def label(colors):
    all_colors = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    color1 = colors[0]
    color2 = colors[1]
    color3 = colors[2]
    
    value1 =all_colors.index(color1)
    value2 =all_colors.index(color2)
    value3 =all_colors.index(color3) 

    resistance = (value1 * 10 + value2) * 10**value3
    if resistance < 1000:
        return f'{resistance} ohms'
    elif resistance < 1000_000 :
        return f'{resistance // 1000} kiloohms'
    elif resistance < 1000_000_000:
        return f'{resistance // 1000_000} megaohms'
    else:
        return f'{resistance // 1000_000_000} gigaohms'
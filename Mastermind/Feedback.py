def feedback(gok, code):
    wit = witP(gok, code)
    zwart = zwartP(gok, code)
    wit = wit - zwart
    return zwart, wit

def witP(gok, code):
    wit = 0
    wit_list = code[:]
    for x in gok:
        if x in wit_list:
            wit_list.remove(x)
            wit = wit + 1
    return wit

def zwartP(gok, code):
    zwart = 0
    zwart_list = code[:]
    teller = 0
    for i in gok:
        if i == zwart_list[teller]:
            zwart = zwart + 1
        teller += 1
    return zwart
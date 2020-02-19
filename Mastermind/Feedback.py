# Functie feedback is de functie zwartP en witP bij elkaar om de juiste feedback te geven.
def feedback(gok, code):
    wit = witP(gok, code)
    zwart = zwartP(gok, code)
    wit = wit - zwart
    return zwart, wit

# Functie voor de witte pin. Toont aan hoeveel cijfers er in de secret code voorkomen.
def witP(gok, code):
    wit = 0
    wit_list = code[:]
    for x in gok:
        if x in wit_list:
            wit_list.remove(x)
            wit = wit + 1
    return wit

# Functie zwartP is voor de zwarte pinnen. Die toont aan hoeveel cijfers er op de juiste positie staan.
def zwartP(gok, code):
    zwart = 0
    zwart_list = code[:]
    teller = 0
    for i in gok:
        if i == zwart_list[teller]:
            zwart = zwart + 1
        teller += 1
    return zwart
def pyramide():
    grote = int(input('Hoe groot?: '))
    for i in range (1, grote+1):
        print(i* '*')
    for a in range (grote-1, 0, -1):
        print(a*'*')
pyramide()

def piramide_while():
    lengte = int(input("Noem een getal: "))
    sterretje = "*"
    start = 0
    while lengte > start:
        b = start * sterretje
        start = start + 1
        print(b)

    while lengte > 0:
        a = lengte * sterretje
        lengte = lengte - 1
        print(a)
piramide_while()
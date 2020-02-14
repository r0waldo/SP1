import random

def gokker():
    n1 = random.randint(0, 6)
    n2 = random.randint(0, 6)
    n3 = random.randint(0, 6)
    n4 = random.randint(0, 6)
    code = []
    code.append(n1)
    code.append(n2)
    code.append(n3)
    code.append(n4)
    print(code)

    while True:
        gok1 = int(input('Gok voor cijfer 1: '))
        gok2 = int(input('Gok voor cijfer 2: '))
        gok3 = int(input('Gok voor cijfer 3: '))
        gok4 = int(input('Gok voor cijfer 4: '))
        gok = []
        gok.append(gok1)
        gok.append(gok2)
        gok.append(gok3)
        gok.append(gok4)
        tel = 0
        for x in gok:
            for y in code:
                if x == y:
                    tel = tel + 1
                    break
        print(tel, "cijfers goed geraden."
                   "")

        if gok == code:
            print('Goed geraden! Je bent een echte MasterMind.')
            break
        else:
            print('Probeer opnieuw.')


def regels():
    print('1. Je voert een 4-cijferige code in. \n'
          '2. Heb je een getal die voorkomt in de geheime code zie je # \n'
          '3. Heb je een getal op de juiste plek ingevoerd zie je $')

# def gamemaster():


def menu():
    print("************MASTERMIND**************")

    choice = input("""
    A: GameMaster
    B: Gokker
    C: Regels

    Wat is je keuze: """)

    if choice == "A" or choice =="a":
        gamemaster()
    elif choice == "B" or choice =="b":
        gokker()
    elif choice == 'C' or choice == 'c':
        regels()
    else:
        print("Je kunt alleen kiezen tussen A, B of C.")
        print("Probeer opnieuw")
menu()

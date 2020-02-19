import random
import time
from Feedback import feedback


def gokker():
    pogingen = 10
    # De computer pakt voor elk een random getal tussen de 0 en 6.
    n1 = random.randint(0, 6)
    n2 = random.randint(0, 6)
    n3 = random.randint(0, 6)
    n4 = random.randint(0, 6)
    # Een lege lijst
    code = []
    # Voert de random gekozen getallen in de lijst.
    code.append(n1)
    code.append(n2)
    code.append(n3)
    code.append(n4)

    while True:
        print('====================================')
        # De vraag naar een gok tussen de 0 en 6.
        gok1 = int(input('Gok voor cijfer 1: '))
        gok2 = int(input('Gok voor cijfer 2: '))
        gok3 = int(input('Gok voor cijfer 3: '))
        gok4 = int(input('Gok voor cijfer 4: '))
        # Lege gok lijst
        gok = []
        # Stopt de gekozen getallen in de lege gok lijst.
        gok.append(gok1)
        gok.append(gok2)
        gok.append(gok3)
        gok.append(gok4)
        pogingen -= 1

        time.sleep(0.5)
        print('Je gok was: ' + str(gok))
        time.sleep(0.5)
        print('Je hebt nog ' + str(pogingen) + ' poging(en) over.')

        if pogingen == 0:
            print('Game Over!')
            break

        if gok == code:
            pogingen = pogingen - 8
            print('Goed geraden! Je bent een echte MasterMind.')
            time.sleep(1)
            print('Het koste je maar ' + str(pogingen) + ' poging')
            break
        elif gok != code:
            print('Feedback is: ', feedback(gok, code), '(wit, zwart)')
            print('Probeer opnieuw.')
            time.sleep(1)

# Regels van het MasterMind spel.
def regels():
    print('1. Je voert een 4-cijferige code in. \n'
          '2. Je code bestaat uit de getallen 0 t/m 6 \n')
    time.sleep(1)
    x = input('Terug naar menu? (Y/N): \n')
    if x == 'Y' or x == 'y':
        menu()
    if x == 'N' or x == 'n':
        print('Oke\n')
        time.sleep(1)
        regels()


def gamemaster():
    # De vraag om een secret code in tevoeren die de computer moet raden.
    code = []
    while len(code) < 4:
        secret = int(input("Geef een getal tussen 0 en 6: "))
        if secret > 6:
            print("Ik zei tussen 0 en 6.")
        elif secret < 1:
            print('Ik zei tussen 0 en 6.')
        elif secret <= 6:
            code.append(secret)
    print("Uw geheime code is", code)
    time.sleep(1)
    print("De computer gaat een poginkje wagen.")
    print('====================================')
    time.sleep(2)

    # Algoritme 1 begin
    # Random gok van getallen tussen de 0 en 6.
    gokken = [[a, b, c, d] for a in range(0, 7) for b in range(0, 7) for c in range(0, 7) for d in range(0, 7)]
    leeg = gokken[:]
    pogingen = 0
    for x in gokken:
        pogingen = pogingen + 1
        # Eerste gok is totaal  random van de computer.
        gok1 = random.choice(gokken)
        # Aanroepen van de  functie in een andere py bestand
        feedback1 = feedback(gok1, code)
        # Vergelijking is het aanhouden van de zelfde feedback
        vergelijking = feedback(x, gok1)
        # Is de feedback niet het zelfde haalt de computer die lijst uit de lijst met mogelijke lijsten.
        if vergelijking != feedback1:
            leeg.remove(x)
        else:
            time.sleep(1)
            print('Geraden in ', pogingen, 'poging(en)')
            break
    if pogingen > 10:
        print('De computer heeft uw code niet kunnen raden in 10 pogingen! Proficiat!')
    elif pogingen <= 10:
        print('De computer heeft uw code geraden. Jammer!')
# Algoritme 1 eind

# Menu van het spel.
def menu():
    print('===========================')
    print("        MASTERMIND")
    print('===========================')

    choice = input("""
    A: GameMaster
    B: Gokker
    C: Regels
    ==========
    Wat is je keuze: """)

    if choice == "A" or choice == "a":
        gamemaster()
    elif choice == "B" or choice == "b":
        gokker()
    elif choice == 'C' or choice == 'c':
        regels()
    else:
        print("Je kunt alleen kiezen tussen A, B of C.")
        print("Probeer opnieuw")


menu()

# Bronnen:
# http://terencegaoanalytics.blogspot.com/2017/10/first-python-project-mastermind-game.html
# https://stackoverflow.com/questions/32036100/mastermind-game-in-python
# https://www.geeksforgeeks.org/mastermind-game-using-python/

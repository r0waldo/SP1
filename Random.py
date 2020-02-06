import random
import time
def gokken():

    systeem= random.randrange(0, 9)
    keuze= int(input('Gok een getal tussen 0 en 10: '))
    while True:
        if systeem == keuze:
            print('Juist! U heeft goed gegokt!')
            break
        else:
            print('U heeft fout gegokt. Probeer opnieuw.')
            time.sleep(1)
            gokken()
            break
gokken()

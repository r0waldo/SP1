import time
import random
from Feedback import feedback

def gamemaster():
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

#Algoritme 1 begin
    gokken = [[a,b,c,d] for a in range(0,7) for b in range(0,7) for c in range(0,7) for d in range(0,7)]
    leeg = gokken[:]
    pogingen = 0
    for x in gokken:
        pogingen = pogingen + 1
        gok1 = random.choice(gokken)
        feedback1 = feedback(gok1, code)
        vergelijking = feedback(x, gok1)
        if vergelijking != feedback1:
            leeg.remove(x)
        else:
            time.sleep(1)
            print('Geraden in ', pogingen, 'poging(en)')
            break
    if pogingen > 10:
        print('De computer heeft uw code niet kunnen raden! Proficiat!')
    elif pogingen <= 10:
        print('De computer heeft uw code geraden. Jammer!')
# Algoritme 1 eind
gamemaster()
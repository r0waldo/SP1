import time
import random
from Feedback import feedback

def ag():
    code = []
    while len(code) < 4:
        secret = int(input("Geef een getal tussen 0 en 6: "))
        if secret > 6 :
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

#Eigen Algoritme
    pogingen= 0
    eerste_gok= [1,1,2,2]
    gokken = [[a, b, c, d] for a in range(0, 7) for b in range(0, 7) for c in range(0, 7) for d in range(0, 7)]
    while True:
        pogingen += 1
        if eerste_gok == code:
            print('De computer heeft het in 1 keer geraden.\nMaak het de computer niet te makkelijk. :)')
            break
        wit = int(input('Het aantal witte pinnen: '))
        zwart = int(input('Het aantal zwarte pinnen: '))
        if wit < 4:
            gok2= random.choice(gokken)
        elif wit == 4
ag()
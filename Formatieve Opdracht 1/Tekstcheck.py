def tekstcheck():
    zin1= str(input('De string is: '))
    zin2= str(input('De string is: '))
    for i in range(len(zin1)):
        if zin1[i] != zin2[i]:
            print('Het eerste verschil zit op index:' + str([i]))

tekstcheck()

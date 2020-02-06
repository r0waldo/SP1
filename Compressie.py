def spaties():
    f = open('Compressie.txt', 'rt')
    tabs= f.readlines()
    for x in tabs:
        pe3 = x.strip(' ')
        pe3 = pe3.strip('\n')
        print(pe3)
spaties()
# h
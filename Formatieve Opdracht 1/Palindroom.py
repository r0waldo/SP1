def palindroom():
    woord = str(input('Voer een woord in: '))
    if woord == woord[::-1]:
        print(woord, 'is een palindroom.')
    else:
        print(woord, 'is geen palindroom.')
palindroom()

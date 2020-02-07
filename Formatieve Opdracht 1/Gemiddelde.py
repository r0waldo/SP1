def gemiddelde():
    lijst= input('Geef een lijst nummers met spatie: ')
    split= lijst.split()
    pe3 = 0
    for num in split:
        pe3 += int(num)
        gem = pe3 / (len(split))
    print('Opgetelde = ', pe3)
    print('Gemiddelde = ', gem)

gemiddelde()
# https://pynative.com/python-accept-list-input-from-user/
def caesar():
    alfabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
    caesar_alfabet = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    tekst = str(input("Geef een tekst: "))
    rotatie = int(input("Geef een rotatie: "))

    caesar_tekst = ""
    for i in tekst.upper():
        if i.isalpha(): caesar_tekst += caesar_alfabet[ (alfabet[i] + rotatie)%26 ]
        else: caesar_tekst += i

    print(tekst)
    print(caesar_tekst.lower())
caesar()
# bron: https://gist.github.com/jameslyons/8701593
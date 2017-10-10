invoer= input('Voer een string in: ')
for letters in invoer:
    uitvoer= ord(letters)
    print('{} {} {:x} {:b}'.format(letters, uitvoer, uitvoer, uitvoer))

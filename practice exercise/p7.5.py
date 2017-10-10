namenLijst = []
aantalVoorkomens  = {}
def namen():
    while True:
        xyz = str(input('Volgende naam: '))
        if xyz == '':
            break
        else:
            namenLijst.append(xyz)
    for x in namenLijst:
        if x not in aantalVoorkomens:
            aantalVoorkomens[x] = 1
        else:
            aantalVoorkomens[x] = aantalVoorkomens[x] + 1

    for x in aantalVoorkomens:
        if aantalVoorkomens[x] >= 2:
            print('Er zijn ' + str(aantalVoorkomens[x]) + ' studenten met de naam ' + x)

        else:
            print('Er is ' + str(aantalVoorkomens[x]) + ' student met de naam ' + x)

namen()

def seizoen(maandnummer):
    if maandnummer > 0 and maandnummer <13:
            if maandnummer >= 3 and maandnummer <= 5:
               print('Lente')
            elif maandnummer >= 6 and maandnummer <= 8:
               print('Zomer')
            elif maandnummer >= 9 and maandnummer <= 11:
               print('herfst')
            else:
               print('Winter')
    else:
        print('Your crazy man!!!!')
        return maandnummer

maandnummer= eval(input('Voer het maandnummer in: '))
seizoen(maandnummer)

try:
    bedrag = 4256
    aantal = eval(input('Geef een aantal: '))
    if bedrag < 0:
        print('Het gegeven getal kan niet.')
    else:
        print(bedrag/aantal)

except ZeroDivisionError:
    print('Delen door 0 kan niet.')

except NameError:
    print('Voer cijfers in.')

except:
    print('Ongeldige invoer.')

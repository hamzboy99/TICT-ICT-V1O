leeftijd = eval(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort: ')
ja = True
nee = False

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')

if leeftijd < 18 or paspoort == 'nee':
    print('Je mag niet stemmen.')

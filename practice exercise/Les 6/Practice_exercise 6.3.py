invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst= invoer.split('-')
slijst= lijst.sort()
grootste_getal= max(lijst)
kleinste_getal= min(lijst)
aantal= len(lijst)
som=0
for getallen in lijst:
    som= som + int(getallen)
gemiddelde= som / aantal

print('Gesorteerde list van ints: {}'.format(lijst))
print('Grootste getal: {} en Kleinste getal: {}'.format(grootste_getal, kleinste_getal))
print('Aantal getallen: {} en Som van de getallen: {}'.format(aantal, som))
print('Gemiddelde: {}'.format(gemiddelde))

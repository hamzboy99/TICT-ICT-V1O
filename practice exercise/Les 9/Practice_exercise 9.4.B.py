import csv

with open('artikel.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter = ';')
    duurste_artikel = 0
    for row in reader:
        prijs = float(row['prijs'])
        if prijs > duurste_artikel:
            duurste_artikel = prijs
            duurste_naam = row['naam']
    print('Het duurste artikel is {} en die kost {} Euro.'.format(duurste_naam, duurste_artikel))

import csv

with open('artikel.csv', 'w', newline = '') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter = ';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('Voer het artikelnummer in: ')
        if artikelnummer == ' ':
            break
        artikelcode = input('Voer de artikelcode in: ')
        naam = input('Voer de naam in: ')
        voorraad = input('Voer de voorraad in: ')
        prijs = input('Voer de prijs in: ')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))

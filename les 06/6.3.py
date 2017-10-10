gegevens= input('Voer een zin in: ')
woorden= gegevens.split()
acroniem= ''
for woord in woorden:
    acroniem= acroniem + woord[0].upper()
print(acroniem)

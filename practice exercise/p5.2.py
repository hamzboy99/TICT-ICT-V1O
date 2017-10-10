infile = open ('kaartnummersuit.txt', 'r')
regels= infile.readlines()
for regel in regels:
    kaartinfo= regel.split(',')
    print('{} heeft kaartnummer: {}'.format(kaartinfo[1].strip(), kaartinfo[0]))
infile.close()


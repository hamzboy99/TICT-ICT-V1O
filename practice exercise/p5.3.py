infile = open('kaartnummers.txt', 'r')
regels= infile.readlines()
aantal= len(regels)
grootstenummer= 0
regelgrootstenummer= 0
regelnummer=0
for regel in regels:
    kaartnummer=regel.split(':')
    aantalkaart= int(kaartnummer[1])
    if grootstenummer < aantalkaart:
        grootstenummer = aantalkaart
        regelgrootstenummer= infile.readline(aantalkaart)
        regelgrootstenummer = regelnummer

print('Deze file telt {} regels. Het grootste kaartnummer is {} en dat staat op regel {} '.format(aantal, grootstenummer, regelgrootstenummer))

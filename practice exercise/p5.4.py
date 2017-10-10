import datetime
outfile = open('hardlopers.txt', 'w')
naam = input("Naam vd hardloper: ")
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
outfile.write('{} , {}'.format(s,naam))
print(s + ', ' + naam)

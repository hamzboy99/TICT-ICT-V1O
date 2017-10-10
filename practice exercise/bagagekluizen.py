print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Geef kluis terug')

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen=len(kluizendata)
    aantalvrij=12-aantalkluizen
    print(aantalvrij)

def kluis_openen():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer=input('geef een kluisnummer: ')
    code=input('wat is je code: ')
    gegevenscorrect=False
    for kluis in kluizendata:
        gegevensvan1kluis=kluis.split(';')
        stringkluisnummer=gegevensvan1kluis[0]
        kluiscode=gegevensvan1kluis[1].strip()
        if stringnummer==stringkluisnummer and code == kluiscode:
            gegevenscorrect=True

    if gegevenscorrect:
        print('kluis is geopend')
    else:
        print('kluis of wachtwoord incorrect')

def kluis_teruggeven():
    # het inlezen van kluizen.txt in een list kluizendata met readlines()
    # elk element van de lijst is een regel uit kluizen.txt
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    # vraag aan de gebuiker het nummer van de kluis
    stringnummer = input('Wat is het nummer van je kluis: ')
    # vraag aan de gebuiker de code van de kluis
    code = input('Wat is de code van je kluis: ')
    # er wordt een nieuw lege lijst aangemaakt. In deze lijst worden alle gegevens van
    # het invoerbestand gestopt, behalve die van de kluis die teruggegevens wordt.
    nieuwekluizendata = []
    # alle regels van het tekstbestand worden doorlopen
    for kluis in kluizendata:
        # doorlopen van kluizendata en elke regel van kluizendata splitsen op ';'
        datavan1kluis = kluis.split(';')
        # elke regel bestaat uit twee elementen waarvan het 1e element het nummer is van het type string;
        stringkluisnummer = datavan1kluis[0]
        # het tweede element is de kluiscode met \n erachter. Die gaat eraf m.b.v. strip.
        kluiscode = datavan1kluis[1].strip()
        # gegevenscorrect is true als nummer en code overeenkomen
        gegevenscorrect = (stringkluisnummer == stringnummer) and (kluiscode == code)
        # als de gegevens niet overeen komen, worden de gegevens aan de lijst nieuwekluizendata toegevoegd
        if not gegevenscorrect:
            # elk element van deze lijst bestaat uit een (string)nummer en een code gescheiden door puntkomma.
            nieuwekluizendata.append(stringkluisnummer + ';' + kluiscode)
    # de list nieuwekluizendat bevat nu alle regels van het invoerbestand, behalve van de kluis
    # die teruggegeven is.
    # Het bestand kluizen.txt wordt nu geopend, maar dan voor schrijven.
    # De bestaande inhoud is hiermee gewist
    outfile = open('kluizen.txt', 'w')
    for i in range(0, len(nieuwekluizendata)):
        # alle elementen worden weggeschreven. Door \n komt ieder volgend element op een volgende regel terecht.
        outfile.write(nieuwekluizendata[i] + '\n')
    # het bestand wordt gesloten.
    outfile.close()

def nieuwe_kluis():
    # maak een lijst met de getallen 1 tot en met 12 die de kluisnummers voorstellen
    kluisnummers = []
    for i in range (1, 13):
        kluisnummers.append(i)

    # het inlezen van kluizen.txt in een list kluizendata met readlines()
    # elk element van de lijst is een regel uit kluizen.txt
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()

    # alle regels van kluizendata worden doorlopen
    for kluis in kluizendata:
        # doorlopen van kluizendata en elke regel van kluizendata splitsen op ';'
        gegevensvan1kluis = kluis.split(';')
        # elke regel bestaat uit twee elementen waarvan het 1e element het nummer is;
        # let op: dit element komt uit een bestand en is dus een string, vandaar stringnummer
        stringnummer = gegevensvan1kluis[0]
        # stringnummer converteren naar een int en toekennen aan nummer
        nummer = int(stringnummer)
        # het element met de waarde nummer uit kluizendata verwijderen
        kluisnummers.remove(nummer)

    # nu bevat kluizendata alleen nummers die nog niet in gebruik zijn
    if len(kluisnummers) > 0:
        # pak het eerste element van kluizendata en dit is het nummer van de kluis
        nieuwkluisnummer = kluisnummers[0];
        # laat dit nummer aan de gebruiker weten
        print('Je kluisnummer is {}'. format(nieuwkluisnummer))
        # vraag de gebruiker om een code in te voeren
        code = input('Voer een code in: ')
        # open het bestand kluizen.txt om een nieuwe kluis toe te voegen met append
        outfile = open('kluizen.txt', 'a')
        # schrijf het nummer en de code in het tekstbestand gescheiden door een ';'
        # omdat append is gebruikt, worden nummer en code achteraan het bestand toegevoegd
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        # sluit het tekstbestand
        outfile.close()
    else:
        # alle kluizen zijn bezet
        print('Er is geen kluis meer beschikbaar')



while True:
 keuze = eval(input('geef een keuze: '))
 if keuze==1:
    toon_aantal_kluizen_vrij()

 elif keuze==2:
    nieuwe_kluis()

 elif keuze==3:
    kluis_openen()

 elif keuze==4:
    kluis_teruggeven()

 else:
    print('u heeft geen geldige optie gekozen')

keuze= eval(input('Maak keuze'))


def standaardprijs(afstandkm):
    prijs=0
    if afstandkm < 0:
        prijs= 0
    if afstandkm > 50:
        prijs= (afstandkm * 0.60) + 15
    if afstandkm <= 50 and afstandkm > 0:
        prijs= afstandkm* 0.80
    return prijs

def ritprijs(leeftijd, weekendrit, afstandkm):
    prijs= standaardprijs(afstandkm)
    if weekendrit:
        if leeftijd < 12 or leeftijd > 64:
           prijs= prijs * 0.65
        else:
           prijs= prijs * 0.60
    else:
        if leeftijd < 12 or leeftijd > 64:
            prijs= prijs * 0.70
        else:
            prijs= prijs * 1
    return '€' + format(prijs, '.2f')
print('Welkom bij de NS')
print('Vul hieronder uw gegevens in.')
print(ritprijs(eval(input("Leeftijd: ")), eval(input("Weekendrit? ")), eval(input("Afstand in KM: "))))






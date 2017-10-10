bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', "Helmond \n't Hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

overeenkomst = bruin.intersection(groen)
verschillen = bruin.difference(groen)
totaal = bruin.union(groen)
print("Overeenkomst: ",overeenkomst)
print("Verschil: ",verschillen)
print("Alle Stations: ",totaal)

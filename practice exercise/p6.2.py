def lijst4string(lst):
    lijst= []
    for woord in lst:
        if len(woord) == 4 and len(lst) == 10:
             lijst.append(woord)
    print(lijst)

lijsttien= eval(input("Geef een lijst met minimaal 10 strings: "))
lijst4string(lijsttien)

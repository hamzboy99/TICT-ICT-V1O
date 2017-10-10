def gemiddelde(lengte):
    aantal= len(str(lengte))
    woorden= len(lengte.split())
    zin= aantal / woorden
    print(zin)

lengte= input('Voer een random zin in: ')
gemiddelde(lengte)

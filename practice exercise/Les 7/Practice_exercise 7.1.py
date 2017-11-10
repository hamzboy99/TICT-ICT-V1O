lst = []
i = 1
while i != 0:
    i =  eval(input('Geef een getal: '))
    if i != 0:
        lst.append(i)

lengte = len(lst)
aantal = sum(lst)

print('Er zijn ' + str(lengte) + ' getallen ingevoerd, de som is: ' + str(aantal))

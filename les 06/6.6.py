lst = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
aantalrijen = len(lst)
aantalkolommen = len(lst[0])
aantalpixels=1
for rij in range(aantalrijen):
    for kolom in range(aantalkolommen):
        if lst [rij][kolom] > 0:
            aantalpixels += 1
    print(aantalpixels)


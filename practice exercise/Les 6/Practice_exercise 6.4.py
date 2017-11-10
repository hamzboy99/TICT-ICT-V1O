studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    lst=[]
    for getallenlijst in studentencijfers:
        gemiddelde= sum(getallenlijst) / len(getallenlijst)
        lst.append(gemiddelde)
    return lst

def gemiddelde_van_alle_studenten(studentencijfers):
    lst=[]
    for getallen in studentencijfers:
        for getal in getallen:
            lst.append(getal)
        antw = int(sum(lst) / len(lst))
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))

som=0
def berekensomevengetallen(som):
   for getallen in getallenrij:
      if getallen % 2==0:
        som= som + getallen
   return som

osom= 0
def berekensomonevengetallen(osom):
    for getallen in getallenrij:
        if getallen %2==1:
            osom= osom+ getallen
    return osom

getallenrij= [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
print('De som van de even getallen bedraagt {}'.format(berekensomevengetallen(som)))
print('De som van de oneven getallen bedraagt {}'.format(berekensomonevengetallen(osom)))

som=0
def berekensomevengetallen(som):
   for getallen in getallenrij:
      if getallen % 2==0:
        som= som + getallen
   print(som)

getallenrij= [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
berekensomevengetallen(som)
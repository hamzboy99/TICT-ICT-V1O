import random
def monopolyworp(dobbelsteen):
    dobbelsteen1 = random.randrange(1,7)
    dobbelsteen2 = random.randrange(1,7)
    somDobbelstenen = dobbelsteen1 + dobbelsteen2
    teller = 0
    while dobbelsteen1 == dobbelsteen2:
        if teller == 3:
            print("direct naar gevangenis")
            break
        else:
            teller += 1
    print(str(dobbelsteen1), '+', str(dobbelsteen2, somDobbelstenen))



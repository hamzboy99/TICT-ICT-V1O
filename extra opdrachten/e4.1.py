invoer= eval(input('Welke temeratuur is het vandaag: '))
if invoer <= 0:
    print('Het vriest vandaag')
elif invoer >=0 and invoer <= 15:
    print('Het is koud vandaag')
else:
    print('Het is lekker weer vandaag ')

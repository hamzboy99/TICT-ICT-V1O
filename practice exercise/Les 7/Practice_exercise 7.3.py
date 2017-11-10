cijfers = {'Pieter': 3.5, 'Kees': 2.3, 'Jasper': 8.6, 'Daan': 9.1, 'Niels': 10, 'Kevin': 4.8, 'Jan': 5.4, 'Nienke': 8.3}
for afkorting in cijfers:
    if cijfers[afkorting] > 8.9:
        print('Naam: {}, cijfer: {}'.format(afkorting, cijfers[afkorting]))

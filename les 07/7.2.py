week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do':'donderdag','vr': 'vrijdag'}
week['di'] = 'dinsdag'
week['za'] = 'zaterdag'
week['zo'] = 'zondag'
for afkorting in week.keys():
    print(afkorting)
for langeNaam in week.values():
    print(langeNaam)
for afkorting in week.keys():
    print(afkorting, week[afkorting])
for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))



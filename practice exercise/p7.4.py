document= open('tickersymbool.txt')
read = document.read().splitlines()
lst = {}

for x in read:
    y = x.split(':')
    lst[y[1]] = y[0]

for x in lst:
    company= (input('Enter Company name: '))
    if company == lst[x]:
        print('Ticker symbol: ' + x)
    else:
        symbool= input('Enter Ticker symbool: ')
        print('Company name: ' + lst[x])


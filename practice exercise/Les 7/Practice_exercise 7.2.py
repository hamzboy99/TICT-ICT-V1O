letters= ''
while len(letters) != 4:
    letters = input('Geef een string van vier letters: ')
    if len(letters) != 4:
        print(letters + ' heeft  ' + str(len(letters)) + ' letters')

print()
print('Inlezen van correcte string: ' + letters + ' is geslaagd')

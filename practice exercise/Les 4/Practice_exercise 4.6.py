def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)
#-omdat de lijst immutable is
#-wel, want string is mutable
#-immutabiliteit

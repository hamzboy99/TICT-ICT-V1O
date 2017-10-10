def diceprob(invoersom):
  aantalworpeninv= 0
  aantalworpen= 0
  while aantalworpeninv < 100:
      import random
      aantalogen1= random.randrange(1, 7)
      aantalogen2= random.randrange(1, 7)
      som= aantalogen1 + aantalogen2
      if som == invoersom:
         aantalworpeninv += 1
      aantalworpen += 1
  print('Het aantal benodige worpen is {}'.format(aantalworpen))

somaantalogen = eval(input('Hoe groot is de som: '))
diceprob(somaantalogen)


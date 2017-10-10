def eindbedrag(invoer_bedrag, invoer_rente):
    uitkomst= invoer_bedrag + invoer_rente + invoer_bedrag / 100
    print(uitkomst)
    return uitkomst

invoer_bedrag= eval(input('Voer een bedrag in: '))
invoer_rente= eval(input('Voer een rente percentage: '))
eindbedrag(invoer_bedrag, invoer_rente)

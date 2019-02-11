naam = input('Hallo, wat is je naam: ')
leeftijd = int(input('Oke ' + naam + ' ,wat is je leeftijd: '))
paspoort = input('Ben je in het bezit van een Nederlands paspoort: ')
if leeftijd >= 18 and paspoort == 'ja':
    print('Je mag stemmen!')
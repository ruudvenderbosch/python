while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord, len(woord)))
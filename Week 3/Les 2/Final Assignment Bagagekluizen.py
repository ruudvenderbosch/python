def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt')
    lstregels = infile.readlines()
    aantalkluizen = 12 - len(lstregels)
    return aantalkluizen
    infile.close

def nieuwe_kluis():
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.txt')
    regels = infile.readlines()
    infile.close()
    for regel in regels:
        onderdelen = regel.split(';')
        kluisnummer = int(onderdelen [0])
        kluisnummers.remove(kluisnummer)
    kluisnummer = kluisnummers[0]
    code = input('Geef een vier cijfige code op?: ')
    infile = open('kluizen.txt', 'a')
    infile.write(str(kluisnummer) + ';' + str(code) + str('\n'))
    print('Kluisnummer {} met code {} is toegewezen.'.format(str(kluisnummer), code))
    infile.close()

def kluis_openen():
    infile = open('kluizen.txt')
    nummer = input('Wat is uw kluisnummer?: ')
    ww = input('Wat is de code?: ')
    regels = infile.readlines()
    infile.close()
    for regel in regels:
        code = regel[2] + regel[3] + regel[4] + regel[5]
        if nummer == regel[0] and ww == code:
            print('Uw kluis met nummer ' + nummer + ' is geopend.')
        else:
            print('Foutmelding! probeer opnieuw!')

def kluis_teruggeven():
    nummer = input('Wat is uw kluisnummer?: ')
    code = input('Wat is uw code in: ')
    invoer = nummer + ";" + code
    te_verwijderen_kluis = nummer + ";" + code + "\n"

    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()

    infile = open('kluizen.txt', 'w')
    for regel in regels:
        if invoer == regel:
            regel = regel.strip()
            regels.remove(te_verwijderen_kluis)
            print('De kluis is geopend en verwijderd.')
            break
        else:
            print('Foutmelding! probeer opnieuw!.')
    infile.close()


print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
      '2: Ik wil een nieuwe kluis\n'
      '3: Ik wil even iets uit mijn kluis halen\n'
      '4: Ik geef mijn kluis terug\n') #optioneel, mag maar hoeft niet

keuze = int(input('Maak uw keuze: '))

if keuze == 1:
    print(toon_aantal_kluizen_vrij())
elif keuze == 2:
    print(nieuwe_kluis())
elif keuze == 3:
    print(kluis_openen())
elif keuze == 4:
    print(kluis_teruggeven())
else:
    print('FOUTMELDING: kies een nummer tussen de 1 t/m 4')


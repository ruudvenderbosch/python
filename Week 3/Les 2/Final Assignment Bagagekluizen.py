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
    code = input('wat wilt u als code?: ')
    infile = open('kluizen.txt', 'a')
    infile.write(str(kluisnummer) + ';' + code + str('\n'))
    print('Kluisnummer {} met code {} is toegewezen.'.format(str(kluisnummer), code))
    infile.close()

print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
      '2: Ik wil een nieuwe kluis\n'
      '3: Ik wil even iets uit mijn kluis halen\n'
      '4: Ik geef mijn kluis terug\n') #optioneel, mag maar hoeft niet

keuze = int(input('Maak uw keuze: '))

if keuze == 1:
    vrijekluizen = toon_aantal_kluizen_vrij()
    print(vrijekluizen)
elif keuze == 2:
    nieuwkluis = nieuwe_kluis()
    print(nieuwkluis)
elif keuze == 3:
    openkluis = kluis_openen()
    print(openkluis)
elif keuze == 4:
    teruggevenkluis = kluis_teruggeven()
    print(teruggevenkluis)
else:
    print('FOUTMELDING: kies een nummer tussen de 1 t/m 4')
    false


infile = open('Kaartnummers.py')
content = infile.read()
infile.close

for line in content.splitlines():
    kaartnummer, klant = line.split(',')
    print('{} heeft kaartnummer: {}'.format(klant, kaartnummer))
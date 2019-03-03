getallen = []

while True:
    getal = int(input('Geef een getal: '))
    if getal > 0 or getal < 0:
        getallen.append(getal)
    else:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallen), sum(getallen)))
        break
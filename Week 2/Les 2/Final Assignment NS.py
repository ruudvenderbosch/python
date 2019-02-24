def standaardprijs(afstandKM):
    if afstandKM < 0:
        return(0)
    else:
        kost1 = afstandKM * 0.8
        if afstandKM <= 50:
            return(kost1)
        else:
            kost2 = 15 + int(afstandKM) * 0.6
            return (kost2)

afstand = int(input('hoeveel kilometer legt u af? '))
leeftijd = int(input('Wat is uw leeftijd? '))
dag = input('Op welke dag ben je van plan om te gaan reizen? ')

def ritprijs (leeftijd, weekendrit, afstandKM):
    x = standaardprijs(afstand)
    return(x)
    dag = input('Op welke dag ben je van plan om te gaan reizen? ')
    if dag == ['zaterdag', 'zondag']:
        if int(leeftijd) < 12 and >= 65:
            prijs1 = x * 0,65
            return (prijs1)
        else:
            prijs2 = x * 0,60
            return (prijs2)
    else:
        if leeftijd < 12 and >= 65:
            prijs3 = x * 0,70
            return (prijs1)
        else:
            prijs2 = x
            return (prijs2)
print(ritprijs)





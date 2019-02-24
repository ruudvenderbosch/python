def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM < 0:
        return prijs

    if afstandKM > 50:
        prijs = 15 + 0.6 * afstandKM
    else:
        prijs = 0.8 * afstandKM
    return prijs


def ritprijs(leeftijd, weekendrit, afstand):
    standaardPrijs = standaardprijs(afstand)
    korting = 1
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 'ja':
            korting -= 0.3
        else:
            korting -= 0.35
    else:
        if weekendrit == 'ja':
            korting -= 0.4
        else:
            korting -= 0
    return standaardPrijs * korting


leeftijd = int(input("Wat is uw leeftijd?: "))
weekendrit = input("Is het een weekendrit: ")
afstandKM = int(input("Wat is de te reizen afstand: "))

print(ritprijs(leeftijd, weekendrit, afstandKM))

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = list(map(int, invoer.split('-')))
lijst.sort()
maximaal = max(lijst)
minimaal = min(lijst)
gemiddelde = sum(lijst) / len(lijst)
som = sum(lijst)
aantal = len(lijst)

print("Gesorteerde lijst van ints: {} \nGrootste getal: {} en Kleinste getal: {} \nAantal getallen: {} en Som van de getallen: {} \nGemiddelde: {}".format(lijst, maximaal, minimaal, aantal, som, gemiddelde))
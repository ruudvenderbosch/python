boodschappen = input(eval("Geef lijst met minimaal 10 strings: "))

vierboodschappen = []
#rekent uit welke strings uit de list bestaan uit 4 letters.
for string in boodschappen:
    if len(string) == 4:
        vierboodschappen.append(string)

print(vierboodschappen)
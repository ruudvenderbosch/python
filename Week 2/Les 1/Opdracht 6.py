s = "Guido van Rossum heeft programmeertaal Python bedacht."
nieuwezin = ""
for letter in s:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        nieuwezin+=letter
    else:
        nieuwezin+='-'

print(nieuwezin)

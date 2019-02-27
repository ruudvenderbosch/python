def seizoen(maand):
    if maand in (3, 4, 5):
        return 'lente'
    elif maand in (6, 7, 8):
        return 'zomer'
    elif maand in (9, 10, 11):
        return 'herfst'
    elif maand in (12, 1, 2):
        return 'winter'
print (seizoen(10))
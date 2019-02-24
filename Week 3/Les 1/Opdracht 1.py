def convert(celcius):
    Fahrenheit = celcius * 1.8 + 32
    return Fahrenheit

def table(c):
    for i in range (-30, 50, 10):
        c = c + 10
        f = c*1.8+32
        print('{:6} {:4}'.format (f, c, end=''))

table(-40)

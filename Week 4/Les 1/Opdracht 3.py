cijfers = {
    'Peter':    2,
    'Sjaak':    4,
    'Diederik': 10,
    'Jan':      9,
    'Pieter':   8,
    'Andre':    6,
    'Ruud':     7,
    'Nigel':    10
}



for a, b in cijfers.items():
	if b > 8:
		print('{}, {}'.format(a, b))


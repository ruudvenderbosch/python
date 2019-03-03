company = input('Enter Company name: ')
ticker_symbol = input('Enter Ticket symbol: ')

def ticker (tickersymbol)
	infile = open('tickersymbol.txt', 'r')
	symbols = {}
	for line in infile.readlines():
		company, symbol = line.rstrip().split(':')
		symbols[company] = symbol
	infile.close()
	return symbols


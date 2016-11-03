def printBoard(m):
	line = '----------------------'
	
	for y, row in enumerate(m):
		s = ''
		if y % 3 == 0:
			print line
		for x, ele in enumerate(row):
			if x % 3 == 0:
				s = s + '|'
			s = s + str(ele) + ' '
		s = s + '|'
		print s
	print line


def main():
	m = [[1]*9 for i in range(0,9)]
	printBoard(m)

if __name__ == '__main__':
	main()
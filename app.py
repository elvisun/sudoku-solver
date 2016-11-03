from collections import deque
from Queue import PriorityQueue

def printBoard(m):
	line = '-------------------------'
	print''
	for y, row in enumerate(m):
		s = ''
		if y % 3 == 0:
			print line
		for x, ele in enumerate(row):
			if x % 3 == 0:
				s = s + '| '
			if ele:
				s = s + str(ele) + ' '
			else:
				s = s + '`' + ' '
		s = s + '|'
		print s
	print line


def bts(x, y, count, m, row_remain, col_remain, sqr_remain):
	#printBoard(m)
	if count == 0:
		return m
	while m[y][x] != 0:
		if x == 8:
			y = y + 1
			x = 0
		else:
			x = x + 1
	available = row_remain[y] & col_remain[x] & sqr_remain[y/3*3+x/3]
	for choice in available:
		m[y][x] = str(choice)
		row_remain[y].discard(choice)
		col_remain[x].discard(choice)
		sqr_remain[y/3*3+x/3].discard(choice)
		if bts(x, y, count - 1, m, row_remain, col_remain, sqr_remain):
			return m
		row_remain[y].add(choice)
		col_remain[x].add(choice)
		sqr_remain[y/3*3+x/3].add(choice)
		m[y][x] = 0
	return 0


def getPoss(m):		#get all possible moves
    row_remain = [set(xrange(1,10)) for _ in xrange(9)]
    col_remain = [set(xrange(1,10)) for _ in xrange(9)]
    sqr_remain = [set(xrange(1,10)) for _ in xrange(9)]
    # Find available remaining choices
    count = 0
    for i in xrange(9):
        for j in xrange(9):
            if m[i][j] != 0:
                val = int(m[i][j])
                row_remain[i].discard(val)
                col_remain[j].discard(val)
                sqr_remain[i/3*3+j/3].discard(val)
            else:
                count = count + 1
    #print count
    return (row_remain,col_remain,sqr_remain, count)


def main():
	m = [
	[0,4,3,5,0,0,0,0,2],
	[0,0,2,0,0,4,0,8,3],
	[0,1,0,0,0,0,6,0,0],
	[0,8,0,7,3,0,0,0,5],
	[2,6,0,0,4,5,0,0,0],
	[1,0,0,0,0,8,0,0,0],
	[0,7,0,3,0,0,0,6,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,6,0,7,0,0,0],
	]
	printBoard(m)
	row_remain, col_remain, sqr_remain, count = getPoss(m)
	solved = bts(0, 0, count, m, row_remain, col_remain, sqr_remain)
	printBoard(solved)

if __name__ == '__main__':
	main()
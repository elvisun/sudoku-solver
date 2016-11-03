from collections import deque
from Queue import PriorityQueue

def printBoard(m):
	line = '-------------------------'
	
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

def solve(m):
	d = {}
	count = 9*9
	for y, row in enumerate(m):
		for x, ele in enumerate(row):
			if not ele:
				d[(x,y)] = getPoss(x,y,m)
				count = count - 1
	return bts(0,0,count,m,d)


def bts(x, y, count, m, oldDict):
	d = dict(oldDict)
	if count == 0:
		return 1
	while m[y][x] != 0:
		if x == 8:
			y = y + 1
			x = 0
		else:
			x = x + 1
	a = getPoss(x, y, m)
	for choice in a:
		m[y][x] = choice
		for child in getArcs(x,y,m):
			if choice in d[child]:
				d[child].remove(choice)
		if bts(x, y, count - 1, m, d):
			return 1
		else:
			for child in getArcs(x,y,m):
				d[child].append(choice)
			m[y][x] = 0
	return 0


def getPoss(x,y,m):		#get all possible moves
	if m[y][x]:
		return []
	d = {1,2,3,4,5,6,7,8,9}
	for i in range(0,9):
		if m[y][i] in d:
			d.remove(m[y][i])
		if m[i][x] in d:
			d.remove(m[i][x])
	for i in range(0,3):
		for j in range(0,3):
			if m[y/3*3+i][x/3*3+j] in d:
				d.remove(m[y/3*3+i][x/3*3+j])
	return list(d)

def getArcs(x,y,m):		#get all arcs
	ret = []
	for i in range(0,9):
		ret.append((i,y))
		ret.append((x,i))
	for i in range(0,3):
		for j in range(0,3):
			ret.append((x/3*3+j,y/3*3+i))
	ret = [p for p in ret if p!=(x,y)]	#list comprehension to remove (x,y)
	return ret

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
	solve(m)
	#print getSucessors(3,4,m)

if __name__ == '__main__':
	main()
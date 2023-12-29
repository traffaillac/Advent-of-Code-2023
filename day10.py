from sys import stdin

nb = {'|':((-1,0),(1,0)), '-':((0,-1),(0,1)), 'L':((-1,0),(0,1)), 'J':((-1,0),(0,-1)), '7':((1,0),(0,-1)), 'F':((1,0),(0,1)), '.':()}
grid = [list(s) for s in stdin.read().split()]
ispipe = [['.']*len(row) for row in grid]
Sr, Sc = next((r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell=='S')
ispipe[Sr][Sc] = '+'
_r, _c = Sr, Sc
nbs = tuple((i, j) for i, j in ((-1,0),(1,0),(0,-1),(0,1)) if any(i+_i==j+_j==0 for _i, _j in nb[grid[Sr+i][Sc+j]]))
grid[Sr][Sc] = next(ch for ch, n in nb.items() if n==nbs)
r, c = Sr+nbs[0][0], Sc+nbs[0][1]
while r!=Sr or c!=Sc:
	ispipe[r][c] = '+'
	_r, _c, r, c = r, c, *next((r+i,c+j) for i, j in nb[grid[r][c]] if r+i!=_r or c+j!=_c)
enclosed = 0
for i, (row, pipe) in enumerate(zip(grid, ispipe)):
	depth = 0
	for j, (c, p) in enumerate(zip(row, pipe)):
		if p=='+':
			depth += (-1,0) in nb[c]
		else:
			enclosed += depth & 1
print(enclosed)
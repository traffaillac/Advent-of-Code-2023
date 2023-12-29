from sys import stdin

grid = stdin.read().split()
gears = {}
for i, row in enumerate(grid):
	j = 0
	while True:
		while j < len(row) and not row[j].isdigit(): j += 1
		if j >= len(row): break
		k = j + 1
		while k < len(row) and row[k].isdigit(): k += 1
		for r in range(max(i-1,0), min(i+2,len(grid))):
			for c in range(max(j-1,0), min(k+1,len(row))):
				if grid[r][c] == '*':
					gears.setdefault((r, c), []).append(int(row[j:k]))
		j = k + 1
print(sum(n[0]*n[1] for n in gears.values() if len(n)==2))
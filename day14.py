from sys import stdin

# G = stdin.read().split()
# load = 0
# for c in range(len(G[0])):
# 	s = 0
# 	while s < len(G):
# 		e = next((r for r in range(s, len(G)) if G[r][c]=='#'), len(G))
# 		n = sum(G[r][c]=='O' for r in range(s, e))
# 		load += sum(len(G)-s-i for i in range(n))
# 		s = next((r for r in range(e+1, len(G)) if G[r][c]!='#'), len(G))
# print(load)

G = stdin.read().split()
R, C = len(G), len(G[0])
blank = [list(g.replace('O', '.')) for g in G]
east = [list(g) for g in G]
seen = {}
cycles = 0
key = ''.join(G)
while key not in seen:
	seen[key] = cycles
	# tilt north
	north = [list(b) for b in blank]
	for c in range(C):
		s = 0
		while s < R:
			e = next((r for r in range(s, R) if east[r][c]=='#'), R)
			for i in range(sum(east[r][c]=='O' for r in range(s, e))):
				north[s+i][c] = 'O'
			s = next((r for r in range(e+1, R) if east[r][c]!='#'), R)
	# tilt west
	west = [list(b) for b in blank]
	for r in range(R):
		s = 0
		while s < C:
			e = next((c for c in range(s, C) if north[r][c]=='#'), C)
			for i in range(sum(north[r][c]=='O' for c in range(s, e))):
				west[r][s+i] = 'O'
			s = next((c for c in range(e+1, C) if north[r][c]!='#'), C)
	# tilt south
	south = [list(b) for b in blank]
	for c in range(C):
		s = 0
		while s < R:
			e = next((r for r in range(s, R) if west[r][c]=='#'), R)
			for i in range(sum(west[r][c]=='O' for r in range(s, e))):
				south[e-1-i][c] = 'O'
			s = next((r for r in range(e+1, R) if west[r][c]!='#'), R)
	# tilt east
	east = [list(b) for b in blank]
	for r in range(R):
		s = 0
		while s < C:
			e = next((c for c in range(s, C) if south[r][c]=='#'), C)
			for i in range(sum(south[r][c]=='O' for c in range(s, e))):
				east[r][e-1-i] = 'O'
			s = next((c for c in range(e+1, C) if south[r][c]!='#'), C)
	cycles += 1
	key = ''.join(''.join(l) for l in east)
mod = cycles - seen[key]
east1M = next(k for k, c in seen.items() if c==(1_000_000_000-seen[key])%mod+seen[key])
load = sum(R-r for r in range(R) for c in range(C) if east1M[r*C+c]=='O')
print(load)
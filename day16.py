from sys import stdin

def beam(r, c, dr, dc):
	seen = set()
	stack = [(r, c, dr, dc)]
	while stack:
		pos = stack.pop()
		r, c, dr, dc = pos
		if 0<=r<R and 0<=c<C and pos not in seen:
			seen.add(pos)
			if G[r][c]=='.' or (G[r][c]=='|' and dc==0) or (G[r][c]=='-' and dr==0):
				stack.append((r+dr, c+dc, dr, dc))
			elif G[r][c]=='/':
				stack.append((r-dc, c-dr, -dc, -dr))
			elif G[r][c]=='\\':
				stack.append((r+dc, c+dr, dc, dr))
			elif G[r][c]=='|':
				stack.extend(((r-1, c, -1, 0), (r+1, c, 1, 0)))
			else:
				stack.extend(((r, c-1, 0, -1), (r, c+1, 0, 1)))
	return len({(r, c) for r, c, _, _ in seen})

G = stdin.read().split()
R, C = len(G), len(G[0])
print(max(max(max(beam(r,0,0,1),beam(r,C-1,0,-1)) for r in range(R)),
          max(max(beam(0,c,1,0),beam(R-1,c,-1,0)) for c in range(C))))
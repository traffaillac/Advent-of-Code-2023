from collections import defaultdict
from pprint import pprint
from sys import stdin

M = stdin.read().split()
R, C = len(M), len(M[0])
nb = ((-1,0), (0,-1), (0,1), (1,0))
stop = {(-1,0):'v#', (0,-1):'>#', (0,1):'<#', (1,0):'^#'}
S = [(-1, 1)]
D = {(-1, 1): 0}
E = []
G = defaultdict(dict)
while S:
	r, c = S.pop()
	for dr, dc in nb:
		i, j = r+dr, c+dc
		if 0<=i<R and 0<=j<C and M[i][j] not in stop[dr,dc]:
			i, j = i+dr, j+dc
			steps = 3
			while i<R-1 and M[i][j] not in "^>v<":
				dr, dc = next((di, dj) for di, dj in nb if M[i+di][j+dj]!='#' and (di,dj)!=(-dr,-dc))
				i, j = i+dr, j+dc
				steps += 1
			i, j = i+dr, j+dc
			if (i, j) not in D:
				D[i, j] = 0
				if i<R:
					S.append((i, j))
			E.append(((r, c), (i, j), steps))
			G[r, c][i, j] = G[i, j][r, c] = steps

for _ in range(len(D)-1):
	for u, v, d in E:
		D[v] = max(D[v], D[u]+d)
print(D[R,C-2]-2)

def rec(u, visited):
	if u[0]==R:
		return 0
	l = -R*C
	for v, d in G[u].items():
		if v not in visited:
			l = max(l, d+rec(v, visited|{u}))
	return l
print(rec((-1,1), set())-2)
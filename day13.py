from sys import stdin

res = 0
for g in stdin.read().split("\n\n"):
	G = g.split()
	for r in range(1, len(G)):
		if sum(sum(a!=b for a, b in zip(G[i], G[j])) for i, j in zip(range(r-1,-1,-1), range(r,len(G))))==1:
			res += r * 100
	for c in range(1, len(G[0])):
		if sum(sum(s[i]!=s[j] for s in G) for i, j in zip(range(c-1,-1,-1), range(c,len(G[0]))))==1:
			res += c
print(res)
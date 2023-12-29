from collections import defaultdict
from heapq import heappush, heappop, heapify
from sys import stdin

G = defaultdict(dict)
E = []
for l in stdin:
	u, vs = l.split(": ")
	for v in vs.split():
		G[u][v] = G[v][u] = 1
		E.append((u, v))

def mincut(G):
	s = next(iter(G.keys()))
	A = {s}
	H = [(-w, t) for t, w in G[s].items()]
	heapify(H)
	while True:
		w, t = heappop(H)
		if len(A)==len(G)-1 and t not in A:
			return s, t, -w
		s = t
		A.add(t)
		for u in G[t]:
			if u not in A:
				heappush(H, (-sum(w for v, w in G[u].items() if v in A), u))
def StoerWagner(G):
	sizes = {s:1 for s in G}
	while len(G)>1:
		s, t, w = mincut(G)
		if w==3:
			print(sizes[t]*(sum(sizes.values())-sizes[t]))
		sizes[s] += sizes[t]
		del sizes[t]
		G[s].pop(t, None)
		for u, w in G[t].items():
			if u != s:
				G[s][u] = G[s].get(u, 0)+w
				G[u][s] = G[u].get(s, 0)+w
				G[u].pop(t, None)
		del G[t]
StoerWagner(G)
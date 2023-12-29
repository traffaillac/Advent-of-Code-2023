from math import lcm
from sys import stdin

inst = [int(c=='R') for c in next(stdin).strip()]
N = len(inst)
next(stdin)
G = {}
for l in stdin:
	G[l[:3]] = (l[7:10], l[12:15])
nodes = [n for n in G if n[2]=='A']
cycles = []
for start in nodes:
	n = start
	steps = 0
	visit = {}
	while n not in visit or visit[n]!=steps%N:
		if n not in visit:
			visit[n] = steps%N
		n = G[n][inst[steps%N]]
		steps += 1
	cycles.append(steps-visit[n]%N)
print(lcm(*cycles))
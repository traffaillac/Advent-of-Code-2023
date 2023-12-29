from collections import defaultdict
from functools import cache
from sys import stdin

bricks = []
cols = defaultdict(list)
for i, l in enumerate(stdin.read().split()):
	p, q = l.split('~')
	x, y, z = map(int, p.split(','))
	X, Y, Z = map(int, q.split(','))
	dx, dy, dz = min(max(X-x,-1),1), min(max(Y-y,-1),1), min(max(Z-z,-1),1)
	cubes = []
	while True:
		cubes.append((x, y, z))
		cols[(x, y)].append((z, i))
		if x==X and y==Y and z==Z: break
		x, y, z = x+dx, y+dy, z+dz
	bricks.append(cubes)

below = defaultdict(set)
for col in cols.values():
	col.sort()
	for (_,i),(_,j) in zip(col[1:], col):
		if i != j:
			below[i].add(j)

above = defaultdict(set)
@cache
def fall(i):
	heights = {j:fall(j) for j in below[i]}
	ground = max(heights.values(), default=0)
	below[i] = {j for j,h in heights.items() if h==ground}
	for j in below[i]:
		above[j].add(i)
	dz = ground+1-min(z for x,y,z in bricks[i])
	h = max(z for x,y,z in bricks[i])+dz
	return h
for i in range(len(bricks)):
	fall(i)

s = 0
for i in range(len(bricks)):
	fell = {i}
	stack = [i]
	while stack:
		j = stack.pop()
		for k in above[j]:
			if below[k]<=fell:
				fell.add(k)
				stack.append(k)
	s += len(fell)-1
print(s)